import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


JSON_FOLDER = "\\data\\"

JSON_ADMIN_TEMPLATE = {"owners": [],
                      "volunteers": {},}

JSON_USER_TEMPLATE = {"users": {},
                      "dates": [],}
                    
JSON_USER_CREATE_TEMPLATE = {"total_requests": 0,
                      "accepted_requests": 0,
                      "dates" : []}