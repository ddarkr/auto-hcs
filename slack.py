from slack_webhook import Slack

from custom_time import KST
from env import SLACK_WEBHOOK


def success(message):
    slack = Slack(url=SLACK_WEBHOOK)
    slack.post(text=KST.strftime('%Y.%m.%d') + " 월 자가진단 결과: ✅ 성공",
               attachments=[{
                   "color": "#00b894",
                   "author_name": "✅ " + KST.strftime('%Y.%m.%d'),
                   "title": message,
                   "text": "처리 기준 (KST): " + KST.strftime('%Y-%m-%d %H:%M:%S')
               }]
               )


def failed(message):
    slack = Slack(url=SLACK_WEBHOOK)
    slack.post(text=KST.strftime('%Y.%m.%d') + " 월 자가진단 결과: ⛔️ 실패",
               attachments=[{
                   "color": "#d63031",
                   "author_name": "⛔ " + KST.strftime('%Y.%m.%d'),
                   "title": message,
                   "text": "처리 기준 (KST): " + KST.strftime('%Y-%m-%d %H:%M:%S')
               }]
               )