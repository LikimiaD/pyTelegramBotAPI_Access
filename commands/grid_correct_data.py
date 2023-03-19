import re

def correct_template(message):
    """return telegram_id, start_time, end_time, date"""
    telegram_id = re.search(r'Telegram ID (\d+)', message.message.text)
    telegram_id = telegram_id.group(0)

    time_match = re.search(r'(\d{2}:\d{2}) - (\d{2}:\d{2})', message.message.text)
    start_time = time_match.group(1)
    end_time = time_match.group(2)

    date_match = re.search(r'(\d{2}.\d{2}.\d{4})', message.message.text)
    date = date_match.group(1)

    return telegram_id, start_time, end_time, date