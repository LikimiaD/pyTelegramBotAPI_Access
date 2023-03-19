from datetime import date, timedelta
import requests
import json
class Schedule:
    def __init__(self) -> None:
        pass

    def startDate(self, week = 1):
        today = date.today()
        if (week):
            return today - timedelta(days=today.weekday())
        else:
            start = today - timedelta(days=today.weekday())
            return start + timedelta(days=7)

    def getSchedule(self, room, start):
        url = "https://lk.misis.ru/method/schedule.get"
        PARAMS = {'room': int(room),
                'start_date' : str(start)}
        jsonFile = requests.post(url, params=PARAMS).json()
        daysDict = {}
        for value in jsonFile["schedule_header"].values():
            if "date" in value:
                daysDict[value['date']] = list()
        days = list(daysDict.keys())
        schedule = jsonFile["schedule"]
        for bell in schedule.values():
            for key, day in bell.items():
                if day['type'] == 'lesson' and not day['lessons']:
                    daysDict[days[int(key[-1])-1]].append("{0}-{1}".format(bell['header']['start_lesson'],
                                        bell['header']['end_lesson']))
        return daysDict
    


if __name__ == "__main___":
    x = Schedule
    y = x.startDate()
    print(y)