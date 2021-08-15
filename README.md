# shape-of-voice

Sản phẩm được nộp tại Shecodes Hackathon 2021

## Giới thiệu sản phẩm 

COVID-19, giãn cách xã hội, mọi thứ đã chuyển sang trực tuyến: công việc, trường học, tương tác xã hội và thậm chí là gia đình, người thân. Đối với nhiều người, điều này đã gây ra rất nhiều bất tiện, tuy nhiên những khó khăn này còn tăng lên gấp bội đối với những người bị câm điếc. Vì việc giao tiếp hàng ngày đối với họ vốn dĩ đã gặp nhiều rào cản, nói gì khi mọi thứ chuyển sang online.

Anh Đỗ Hoàng Thái Anh, Chủ tịch Chi hội người điếc Hà Nội (HAD) cho hay: “Theo số liệu thống kê năm 2019, nước ta có khoảng 1,5 đến 2 triệu người người câm điếc và người khiếm thính, tuy nhiên số lượng phiên dịch ngôn ngữ ký hiệu chuyên nghiệp lại chỉ có khoảng hơn 10 người, đây là một sự chênh lệch quá lớn”.
Người điếc khi đi học, tham gia phổ cập giáo dục nếu như không có phiên dịch ngôn ngữ ký hiệu, dĩ nhiên họ không thể hiểu được hết nội dung bài giảng, điều này gây ra sự cản trở lớn trong quá trình tiếp thu kiến thức của mình. Một số ít người điếc có cơ hội, được học lên cao đẳng, đại học nhưng khi thiếu phiên dịch thì họ cũng khó có thể giao tiếp với xung quanh hay ngược lại dù có phiên dịch ngôn ngữ ký hiệu bên cạnh, người điếc cũng không thể tiếp thu được đầy đủ nội dung do trình độ học vấn hạn chế.

Điều này trên thực tế là do mọi thứ đã chuyển sang trực tuyến và những nền tảng cuộc gọi điện video truyền thống như Zoom thiếu phụ đề dành cho người câm điếc.
Dự án này sẽ xây dựng một nền tảng họp trực tuyến mới, cho phép người câm điếc truy cập và bày tỏ suy nghĩ của họ với bất kỳ ai thông qua ngôn ngữ ký hiệu tay trong khi những người bình thường có thể nghe và nói với người câm điếc.

## Chức năng

- Chuyển đổi ngôn ngữ kí hiệu sang giọng nói 
- Chuyển đổi giọng nói sang văn bản
- Các model nhận dạng với độ chính xác > 90%

## Công nghệ sử dụng

- Áp dụng thị giác máy tính và học sâu để chuyển đổi ngôn ngữ kí hiệu sang giọng nói: opencv, tensorflow
- Xử lý âm thanh thành text: google api 
- Phát triển web: flask, html, css, bootstrap

## Hướng phát triển tương lai

- Thu thập thêm dữ liệu về ngôn ngữ kí hiệu tiếng việt 
- Phát triển sản phẩm có thể đáp ứng nhu cầu thời gian thực

## Khó khăn khi gặp phải 

- Các thành viên là newbie trong lập trình web 
- Mất nhiều thời gian trong việc thu thập dữ liệu và tìm kiếm thử nghiệm các model 
- Hackathon online tạo ra nhiều rào cản về giao tiếp và làm việc nhóm

## Các kỹ năng học được 

- Lập trình và phát triển web 
- Học được mindset từ việc lên ý tưởng, thử nghiệm và phát triển 1 phần mềm AI
- K

## Cách sử dụng

- Clone repo này về máy và di chuyển vào thư mục repo

- Cài `ffmpeg` tại môi trường sử dụng

VD: Đối với anaconda

```
conda install ffmpeg -y
```

- Cài đặt các thư viện

```
pip install -r requirements.txt
```

- Tải [model weights](https://drive.google.com/file/d/12Cgl9u-WAJZ6WitrPgH20t5J1ookzMSS/view?usp=sharing)

- Chạy server

```
python app.py
```

- Server sẽ chạy tại http://127.0.0.1:5000/
