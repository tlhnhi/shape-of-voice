import cv2
import numpy as np
import math
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from sklearn.neighbors import KNeighborsClassifier
import glob
import os
import joblib

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class Sign2Text:
    def __init__(self, cnn_model_path, knn_model_path, unsupervised_data_dir=None):
        print('Loading model: ', cnn_model_path)
        self.cnn_model = load_model(cnn_model_path)
        self.classes_supervised = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']
        self.en_vn_dict = {
            'Good job': 'Amazing good job em!',
            'i love you': 'Tôi yêu các bạn',
            'ok': 'Đồng ý'
        }
        self.knn = joblib.load(knn_model_path)
        self.feature_extractor = VGG16(weights='imagenet', include_top=False)
        print('Model is loaded sucessfully')
        if unsupervised_data_dir != None:
            X_train, y_train = self.load_unsupervised_data(unsupervised_data_dir)
            X_train = self.feature_extractor.predict(X_train, batch_size=4)
            X_train = X_train.reshape(len(X_train), -1)
            self.knn = KNeighborsClassifier(n_neighbors=10, weights='distance')
            self.knn.fit(X_train, y_train)
        
    def load_unsupervised_data(self, unsupervised_data_dir):
        print('Load data from :', unsupervised_data_dir)
        images = []
        labels = []
        for f in glob.glob(unsupervised_data_dir + '/*/*.jpg'):
            image = cv2.imread(f, 1)
            image = cv2.resize(image, (224, 224))
            images.append(image)
            label = f.split('/')[-2]
            labels.append(label)
        images = np.array(images)
        labels = np.array(labels)
        print('Images shape: ', images.shape)
        return images, labels

    def predict_cnn(self, img):
        img = cv2.resize(img, (75, 75))
        img = img*1.0/255
        img = np.reshape(img, (1, 75, 75, 3))
        pred_arr = self.cnn_model.predict(img)[0]
        pred_prob = np.max(pred_arr)
        pred_class = self.classes_supervised[np.argmax(pred_arr)]
        return pred_class, pred_prob*100
    
    def predict_knn(self, img):
        img = cv2.resize(img, (224, 224))
        img = np.expand_dims(img, axis=0)
        feature = self.feature_extractor.predict(img).reshape(1, -1)
        pred_class = self.knn.predict(feature)[0]
        pred_proba = np.max(self.knn.predict_proba(feature))
        return pred_class, pred_proba*100

    def predict(self, img):
        pred_class, prob = self.predict_knn(img)
        print('KNN predicts: {} with {:.2f}%'.format(self.en_vn_dict[pred_class], prob))
        if prob >= 70.0:
            return self.en_vn_dict[pred_class], prob
        pred_class, prob = self.predict_cnn(img)
        print('CNN predicts: {} with {:.2f}%'.format(pred_class, prob))
        if prob >= 70.0:
            return pred_class, prob
        return None, None

if __name__ == '__main__':
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 680)

    model = Sign2Text('InceptionResNetV2_10epochs.h5', './Data/')
    data_dir = './Data/i love you'
    indx = len(os.listdir(data_dir))
    while cv2.waitKey(1) != ord('q') :
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        start_point = (200, 200)
        width = 500
        height = 500
        end_point = (start_point[0] + width, start_point[1] + height)
        color = (255, 0, 0)
        thickness = 2
        frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
        
        if cv2.waitKey(1) == ord('c'):
            img = frame[start_point[1]:start_point[1] + height, start_point[0]:start_point[0] + width, :]
            # img = cv2.flip(img, 1)
            pred_class, prob = model.predict(img)
            if pred_class == None:
                print('Try again')
            else:
                print('{} with {:.2f}%'.format(pred_class, prob))
            
        if cv2.waitKey(1) == ord('s'):
            img = frame[start_point[1]:start_point[1] + height, start_point[0]:start_point[0] + width, :]
            cv2.imwrite(data_dir+'/{}.jpg'.format(indx), img)
            print('Save image {}!'.format(indx))
            indx += 1

        cv2.imshow("VideoFrame", frame)

    capture.release()
    cv2.destroyAllWindows()