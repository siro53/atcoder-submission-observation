import requests
import json
import datetime
from config import *

today_dt = datetime.datetime.now()
dt = datetime.datetime(today_dt.year, today_dt.month, today_dt.day)
unix_second = int(dt.timestamp())

for user_id in rival_list:
    # https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md
    url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={user_id}&from_second={unix_second}"
    res = requests.get(url)
    submissions = json.loads(res.text)
    msg = f"{user_id}さんの{dt.date()}の提出は{len(submissions)}件です\n"
    for submission in submissions:
        msg += f"- https://atcoder.jp/contests/{submission['contest_id']}/submissions/{submission['id']}\n"
    send_data = json.dumps({"username": "提出監視bot", "content": msg})
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, send_data, headers=headers)
