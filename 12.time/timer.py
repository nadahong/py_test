import time
import subprocess


def countdown(sec):
    time_left = sec

    while time_left > 0:
        print(time_left, end='..')
        time.sleep(1)
        time_left -= 1


def main():
    howmany_sec = 3
    countdown(howmany_sec)
    # 카운트다운이 끝나면 사운드 파일을 실행한다.
    subprocess.Popen(['start', 'alarm.wav'], shell=True)


if __name__ == '__main__':
    main()
