import requests
import time
import schedule


def telegram_bot_sendtext():

    # bot_token = ''
    # bot_chatID = ''
    # send_text = 'https://api.telegram.org/bot' + "5229778311:AAEcbsxM6lvxzNtAA93i2xxA_P8TQNMpTWU" + '/sendMessage?chat_id=' + "-1001708304911" + '&parse_mode=Markdown&text=' + "Testing Telegram bot"
    # send_text = 'https://api.telegram.org/bot' + "5229778311:AAEcbsxM6lvxzNtAA93i2xxA_P8TQNMpTWU" + '/sendDocument?chat_id=' + "-1001708304911" + '&parse_mode=Markdown&document=' + "https://docs.google.com/document/d/1NE4uYfiGqsnAVYA501numWZGRMfrmJaNmGT4MrbldAY/edit?usp=sharing"

    token = "5229778311:AAEcbsxM6lvxzNtAA93i2xxA_P8TQNMpTWU"
    chat_id = -1001708304911  # chat id
    file = "https://docs.google.com/document/d/1Mv5bVAov6MWH38ENQKMsAccHEToOsp1txUemzP3sOhk/edit?usp=sharing"

    url = f"https://api.telegram.org/bot{token}/sendDocument"
    files = {}
    files["document"] = file
    response = requests.get(url, params={"chat_id": chat_id}, files=files)

    # response = requests.get(send_text)
    print(response.json())

    return response.json()


schedule.every(10).seconds.do(telegram_bot_sendtext)
while True:
    schedule.run_pending()
    time.sleep(1)

print(telegram_bot_sendtext())
