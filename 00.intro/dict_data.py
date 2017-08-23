
addresses = [
    {
        "name": "hong gil dong",
        "email": "hong@naver.com",
        "hp_num": "010-000-000"
    },
    {},
    {},
    {}
]

original = input('input your word: ')

if len(original) > 0 and original.isalpha():
    print(original.lower()[1:] + original.lower()[0] + 'ay')
else:
    print('invalid word')

