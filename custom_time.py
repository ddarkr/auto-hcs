from datetime import datetime
from pytz import timezone

KST = datetime.now(timezone('Asia/Seoul'))


def return_korean_weekday(weekday):
    if weekday == 0:
        return '월'
    if weekday == 1:
        return '화'
    if weekday == 2:
        return '수'
    if weekday == 3:
        return '목'
    if weekday == 4:
        return '금'
    if weekday == 5:
        return '토'
    if weekday == 6:
        return '일'
