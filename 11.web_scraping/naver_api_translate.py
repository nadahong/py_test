import requests


def do_translate(text):
    headers = {
        'X-Naver-Client-Id': '1t0YiqUeuZkkvPFNghNJ',
        'X-Naver-Client-Secret': 'H9F7_fsFS2'
    }
    payload = {
        'source': 'ko',
        'target': 'en',
        'text': text
    }

    req = requests.Request('POST',
                     'https://openapi.naver.com/v1/papago/n2mt',
                     headers=headers, data=payload)
    prepared = req.prepare()
    s = requests.Session()
    res = s.send(prepared)

    result_text = res.json()['message']['result']['translatedText']
    print(result_text)
    return result_text


def main():
    result_list = []
    with open('yesterday.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            if line.strip() == '':
                continue
            result_list.append(do_translate(line))

    with open('yesterday_translated.txt', 'w', newline='', encoding='UTF-8') as result_file:
        for line in result_list:
            result_file.write(line + '\n')

    print('job completed..')


main()


# #bestList > ol > li.num1 > p.copy > a