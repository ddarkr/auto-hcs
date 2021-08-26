# started at 2020.11.17
# 간편한 삶을 위한 자동 자가진단 스크립트

from check import check
from custom_time import KST, return_korean_weekday
import requests

weekday = KST.weekday()


def process():
    print('## 자동 자가진단 process 시작')
    print('오늘의 요일: ' + return_korean_weekday(weekday))

    if weekday == 5 or weekday == 6:
        print('오늘은 ' + return_korean_weekday(weekday) + '요일입니다. 자가진단을 생략합니다.')
    else:
        check()

def checkReq():
    r = requests.get('https://hcs.eduro.go.kr/v2/searchSchool?lctnScCode=01&schulCrseScCode=4&orgName=%EC%9D%B8%EC%B0%BD%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90&loginType=school')
    print(r.text)

if __name__ == '__main__':
    checkReq()
