from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from datetime import datetime, timedelta

def send_mattermost_message(webhook_url, message):
    payload = {
        'text': message
    }
    response = requests.post(webhook_url, json=payload)

    if response.status_code == 200:
        print('Message sent successfully to Mattermost!')
    else:
        print('Failed to send message to Mattermost.')

def schedule_multiple_notifications(webhook_url, messages, times):
    scheduler = BlockingScheduler()

    for i, message in enumerate(messages):
        time = times[i]
        scheduler.add_job(send_mattermost_message, 'cron', day_of_week='mon-fri', hour=time.hour, minute=time.minute, args=[webhook_url, message])

    scheduler.start()


# Mattermost 웹훅 URL 및 전송할 메시지, 반복 시간 설정
webhook_url = 'https://meeting.ssafy.com/hooks/prdwpspz6pgwunzk8or4jxfcor'
messages = ['@here 입실 체크 하세요', '@here 퇴실 체크 하세요 :tiredcat: ', '@here 퇴실 체크 하세요 :tiredcat: ', '@here 퇴실 체크 하세요 :tiredcat: ', '@here 퇴실 체크 하세요 :tiredcat: ']
times = [datetime.strptime(time, '%H:%M') for time in ['20:33','20:34','20:35','20:36','20:37']]

schedule_multiple_notifications(webhook_url, messages, times)
