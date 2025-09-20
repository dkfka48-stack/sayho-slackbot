import schedule
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import os
from dotenv import load_dotenv
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_NAME = os.getenv("CHANNEL_NAME")

client = WebClient(token=SLACK_BOT_TOKEN)

def send_message(text):
    try:
        client.chat_postMessage(channel=CHANNEL_NAME, text=text)
        print(f"✅ 보냄: {text}")
    except SlackApiError as e:
        print(f"❌ 에러: {e.response['error']}")

# 💬 메시지 내용
morning_message = """☀️ 오늘의 할 일을 공유해주세요!
📌 오늘 할 일
🔥 내일 우선순위
😫 방해요소
@쭈노 @모모"""

afternoon_message = """🕓 현재 진행 상황을 공유해주세요!
⭐️ 진행한 것
⚒️ 막힌 점/고민되는 점
🎯 끝낼 오늘의 목표
@쭈노 @모모"""

evening_message = """🌙 오늘 어땠나요? 회고해주세요!
✅ 오늘 한 일
❌ 오늘 못 한 일(이유)
💬 배운 점 1줄 & 회고
@쭈노 @모모"""

# ⏰ Railway는 GMT 기준 → 한국 기준보다 -9시간
schedule.every().day.at("00:00").do(send_message, morning_message)   # 오전 9시
schedule.every().day.at("07:00").do(send_message, afternoon_message) # 오후 4시
schedule.every().day.at("11:00").do(send_message, evening_message)   # 오후 8시

while True:
    schedule.run_pending()
    time.sleep(30)
