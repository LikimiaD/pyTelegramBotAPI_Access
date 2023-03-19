from .json_lib import UserInfo

def is_owner(func):
    def wrapper(message):
        if UserInfo().status_call(message) == "owner":
            return func(message)
        else:
            pass
    return wrapper

def is_volunteer(func):
    def wrapper(message):
        if UserInfo().status_call(message) == "volunteer":
            return func(message)
        else:
            pass
    return wrapper

def is_user(func):
    def wrapper(message):
        if UserInfo().status_call(message) == "user":
            return func(message)
        else:
            pass
    return wrapper