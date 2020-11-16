# started at 2020.11.17
# 간편한 삶을 위한 자동 자가진단 스크립트

from check import check
from custom_time import KST, return_korean_weekday

weekday = KST.weekday()


def process():
    print('## 자동 자가진단 process 시작')
    print('오늘의 요일: ' + return_korean_weekday(weekday))

    if weekday == 5 or weekday == 6:
        print('오늘은 ' + return_korean_weekday(weekday) + '요일입니다. 자가진단을 생략합니다.')
    else:
        check()


if __name__ == '__main__':
    process()
