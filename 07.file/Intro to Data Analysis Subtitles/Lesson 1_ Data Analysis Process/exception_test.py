
try:
    open('abc.txt', 'r')
except FileNotFoundError:
    print('파일이 없어요')
except:
    print('뭔가 섬띵 에러에요..')
