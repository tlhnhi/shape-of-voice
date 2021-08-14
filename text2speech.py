import requests

url = 'https://api.fpt.ai/hmi/tts/v5'

payload = 'xin chào mọi người ở shecodes hackathon'
voice_option = ['leminh', 'banmai', 'thuminh', 'giahuy', 'ngoclam', 'myan', 'lannhi', 'linhsan', 'minhquang']
headers = {
    'api-key': '1AGd8nuJW3sz3qbfyAwqii1XHPrBZAlA',
    'speed': '',
    'voice': voice_option[7]
}

response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)

print(response.text)
