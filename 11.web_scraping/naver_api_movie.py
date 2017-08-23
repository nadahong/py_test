import requests, pprint

headers = {
    'X-Naver-Client-Id': '1t0YiqUeuZkkvPFNghNJ',
    'X-Naver-Client-Secret': 'H9F7_fsFS2'
}

payload = {
    'query': '봉준호',
    'display': 100
}
url = 'https://openapi.naver.com/v1/search/movie.json'
res = requests.get(url, headers=headers, params=payload)

print(res.json())
# res_list = [
#     res.json()['items'][0]['director'][:-1],
#     res.json()['items'][0]['pubDate'],
#     res.json()['items'][0]['title'][3:5],
# ]
#
# print(res_list)
