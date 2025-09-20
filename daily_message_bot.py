{\rtf1\ansi\ansicpg949\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import schedule\
import time\
from slack_sdk import WebClient\
from slack_sdk.errors import SlackApiError\
\
import os\
from dotenv import load_dotenv\
load_dotenv()\
\
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")\
CHANNEL_NAME = os.getenv("CHANNEL_NAME")\
\
client = WebClient(token=SLACK_BOT_TOKEN)\
\
def send_message(text):\
    try:\
        client.chat_postMessage(channel=CHANNEL_NAME, text=text)\
        print(f"\uc0\u9989  \u48372 \u45252 : \{text\}")\
    except SlackApiError as e:\
        print(f"\uc0\u10060  \u50640 \u47084 : \{e.response['error']\}")\
\
# \uc0\u55357 \u56492  \u47700 \u49884 \u51648  \u45236 \u50857 \
morning_message = """\uc0\u9728 \u65039  \u50724 \u45720 \u51032  \u54624  \u51068 \u51012  \u44277 \u50976 \u54644 \u51452 \u49464 \u50836 !\
\uc0\u55357 \u56524  \u50724 \u45720  \u54624  \u51068 \
\uc0\u55357 \u56613  \u45236 \u51068  \u50864 \u49440 \u49692 \u50948 \
\uc0\u55357 \u56875  \u48169 \u54644 \u50836 \u49548 \
@\uc0\u52040 \u45432  @\u47784 \u47784 """\
\
afternoon_message = """\uc0\u55357 \u56659  \u54788 \u51116  \u51652 \u54665  \u49345 \u54889 \u51012  \u44277 \u50976 \u54644 \u51452 \u49464 \u50836 !\
\uc0\u11088 \u65039  \u51652 \u54665 \u54620  \u44163 \
\uc0\u9874 \u65039  \u47561 \u55180  \u51216 /\u44256 \u48124 \u46104 \u45716  \u51216 \
\uc0\u55356 \u57263  \u45149 \u45244  \u50724 \u45720 \u51032  \u47785 \u54364 \
@\uc0\u52040 \u45432  @\u47784 \u47784 """\
\
evening_message = """\uc0\u55356 \u57113  \u50724 \u45720  \u50612 \u46432 \u45208 \u50836 ? \u54924 \u44256 \u54644 \u51452 \u49464 \u50836 !\
\uc0\u9989  \u50724 \u45720  \u54620  \u51068 \
\uc0\u10060  \u50724 \u45720  \u47803  \u54620  \u51068 (\u51060 \u50976 )\
\uc0\u55357 \u56492  \u48176 \u50868  \u51216  1\u51460  & \u54924 \u44256 \
@\uc0\u52040 \u45432  @\u47784 \u47784 """\
\
# \uc0\u9200  Railway\u45716  GMT \u44592 \u51456  \u8594  \u54620 \u44397  \u44592 \u51456 \u48372 \u45796  -9\u49884 \u44036 \
schedule.every().day.at("00:00").do(send_message, morning_message)   # \uc0\u50724 \u51204  9\u49884 \
schedule.every().day.at("07:00").do(send_message, afternoon_message) # \uc0\u50724 \u54980  4\u49884 \
schedule.every().day.at("11:00").do(send_message, evening_message)   # \uc0\u50724 \u54980  8\u49884 \
\
# \uc0\u47336 \u54532 \
while True:\
    schedule.run_pending()\
    time.sleep(30)}