## これは何

ライバルのAtCoderへの提出をdiscordに通知するbot

## 使い方
1. `config.py` に通知したい discord のテキストチャンネルの webhook url と ライバルの AtCoder id を入れます
    - webhook url の取得方法は[こちら](https://zenn.dev/lambta/articles/5edbda4ccb1ec6)が詳しい
2. `main.py` を実行します
3. discord のテキストチャンネルに今日のライバルの提出件数と提出リンクが通知されます