from requests import Request, Session

s = Session()

headers = {
    'X-Naver-Client-Id': 'TVcdGN3l5f8ZIswuZ4tX',
    'X-Naver-Client-Secret': '4F9aWQDSdZ',
}

text = "Somewhere over the rainbow way up high"

payload = {
    'source': 'en',
    'target': 'ko',
    'text': text,
}

url = 'https://openapi.naver.com/v1/language/translate'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()

res = s.send(prepped)

res_json = res.json()
print(res_json)
print(res_json['message']['result']['translatedText'])
