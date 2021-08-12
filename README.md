# shape-of-voice

Shecodes Hackathon 2021

## Môi trường

Web minh họa được phát triển bằng Python 3.9 với các thư viện hỗ trợ như sau:

- **Flask**

```
pip install Flask
```

## Cách sử dụng

- Clone repo này về máy và di chuyển vào thư mục repo

- Export biến môi trường `FLASK_APP` (1 trong 3 cách)
  - Với Bash
  ```
  export FLASK_APP=demo_app.py
  ```
  - Với CMD
  ```
  set FLASK_APP=demo_app.py
  ```
  - Với Powershell
  ```
  $env:FLASK_APP = "demo_app.py"
  ```
- Chạy server

```
flask run
```

- Server sẽ chạy tại http://127.0.0.1:5000/
