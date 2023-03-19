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


def grid_information(message: str):
    cabinet = re.search(r'кабинета\s+(\w+-\d+)', message.message.text).group(1)
    print(f"Cabinet: {cabinet}")

    intervals = len(re.findall(r'с \d{2}:\d{2} до \d{2}:\d{2}', message.message.text))
    print(f"Intervals: {intervals}")

    week = re.search(r'(следующую | текущую)', message.message.text).group(1)
    print(f"Week: {week}")