import json

from .templates.json_templates import *

def check_json(filename):
    if (os.path.isfile(BASE_DIR + JSON_FOLDER + filename)):
        pass
    else:
        with open(BASE_DIR + JSON_FOLDER + filename, "w") as file:
            if filename == "admin_data.json":
                json.dump(JSON_ADMIN_TEMPLATE, file)
            else:
                json.dump(JSON_USER_TEMPLATE, file)

class UserJson:
    def __init__(self) -> None:
        self.admin_filename = "admin_data.json"
        self.user_filename = "user_data.json"
        check_json(self.admin_filename)
        check_json(self.user_filename)
    
    def add_member_status(self, user_id, status):
        try:
            value = True
            with open(BASE_DIR + JSON_FOLDER + self.admin_filename, 'r+') as file:
                file_data = json.load(file)
                if status == 'owner' and user_id not in file_data['owners']:
                    file_data['owners'].append(user_id)
                elif status == 'volunteer' and str(user_id) not in file_data['volunteers']:
                    file_data['volunteers'][str(user_id)] = {'status' : 'offline', 'processed_requests' : 0}
                else:
                    value = False
                file.seek(0)
                json.dump(file_data,file)
            return value
        except Exception:
            return False
    
    def drop_user_data(self):
        with open(BASE_DIR + JSON_FOLDER + self.admin_filename, "w") as file:
            json.dump(JSON_USER_TEMPLATE, file)


class UserInfo(UserJson):
    def member_status_call(self, message):
        with open(BASE_DIR + JSON_FOLDER + self.admin_filename, 'r+') as file:
            file_data = json.load(file)
            if message.from_user.id in file_data['owners']:
                status = "Разработчик"
                return "Информация о пользователе:\n\nИмя: {0}\nВаш ID: {1}\nСтатус: {2}".format(message.from_user.username, message.from_user.id, status)
            elif str(message.from_user.id) in file_data['volunteers']:
                status = "Волонтер"
                return "Информация о пользователе:\n\nИмя: {0}\nВаш ID: {1}\nСтатус пользователя: {2}\nСтатус: {3}\nОбработано заявок: {4}".format(message.from_user.username,
                                                                                                                           message.from_user.id,
                                                                                                                           status,
                                                                                                                           file_data["volunteers"][str(message.from_user.id)]["status"],
                                                                                                                           file_data["volunteers"][str(message.from_user.id)]["processed_requests"])
            else:
                status = "Пользователь"
                return "Информация о пользователе:\n\nИмя: {0}\nВаш ID: {1}\nСтатус: {2}".format(message.from_user.username, message.from_user.id, status)
    
    def status_call(self, message):
        with open(BASE_DIR + JSON_FOLDER + self.admin_filename, 'r+') as file:
            file_data = json.load(file)
            if message.from_user.id in file_data['owners']:
                return "owner"
            elif str(message.from_user.id) in file_data['volunteers']:
                return "volunteer"
            else:
                return "user"
            
    def volunteer_status(self, message):
        with open(BASE_DIR + JSON_FOLDER + self.admin_filename, 'r+') as file:
            file_data = json.load(file)
            status = file_data['volunteers'][str(message.from_user.id)]["status"]
            file_data['volunteers'][str(message.from_user.id)]["status"] = "online" if status == "offline" else "offline"
            file.seek(0)
            file.truncate()
            json.dump(file_data,file)

    def volunteer_online_status(self):
        with open(BASE_DIR + JSON_FOLDER + self.admin_filename, 'r') as file:
            file_data = json.load(file)
            online_list = ""
            for item in file_data['volunteers']:
                if file_data['volunteers'][str(item)]["status"] == "online":
                    online_list += item + "\n"
            if online_list != "":
                text = "На данный момент работают:"
                text += online_list
            else:
                text = "На данный момент никто не работает :c"
            return text
    
    def volunteer_stat(self):
        with open(BASE_DIR + JSON_FOLDER + self.admin_filename, 'r+') as file:
            file_data = json.load(file)
            stat = "Статистика волонтеров:\n\n"
            for item in file_data['volunteers']:
                stat += "ID: {0}\tСтатус: {1}\tОбработанных запросов: {2}\n".format(item,
                                                                                    file_data['volunteers'][str(item)]["status"],
                                                                                    file_data['volunteers'][str(item)]["processed_requests"])
            return stat

    def owner_list_call(self):
        with open(BASE_DIR + JSON_FOLDER + self.admin_filename, 'r+') as file:
            file_data = json.load(file)
            return file_data['owners']
    
    def user_request(self,user_id: str, date: str):
        try:
            with open(BASE_DIR + JSON_FOLDER + self.user_filename, 'r+') as file:
                file_data = json.load(file)
                if user_id not in file_data["users"]:
                    file_data["users"][user_id] = JSON_USER_CREATE_TEMPLATE
                file_data["users"][user_id]["total_requests"] += 1
                file_data["users"][user_id]["dates"].append(date)
                file_data["dates"].append(date)
                file.seek(0)
                json.dump(file_data,file)
            return True
        except:
            return False

            