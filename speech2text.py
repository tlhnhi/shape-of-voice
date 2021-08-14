import requests

url = 'https://api.fpt.ai/hmi/asr/general'
payload = open('shecodes.m4a', 'rb').read()
headers = {
    'api-key': 'COuXM2I8SVpJofP8iFjUiTNmEeJvUwhf'
}

response = requests.post(url=url, data=payload, headers=headers)

print(response.json())
