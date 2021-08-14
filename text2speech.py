import requests

url = 'https://api.fpt.ai/hmi/tts/v5'

input_text = 'xin chào mọi người ở shecodes hackathon'
voice_option = ['leminh', 'banmai', 'thuminh', 'giahuy', 'ngoclam', 'myan', 'lannhi', 'linhsan', 'minhquang']
voice_id = 7 # could be change

headers = {
    'api-key': '1AGd8nuJW3sz3qbfyAwqii1XHPrBZAlA',
    'speed': '',
    'voice': voice_option[voice_id]
}

response = requests.request('POST', url, data=input_text.encode('utf-8'), headers=headers)

print(response.text)
