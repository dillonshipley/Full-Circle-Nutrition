import uuid

class UserDefaults:
    BASE_URL = "/v0/users/"
    USER_ID = uuid.UUID('{f81ee084-9cef-49cc-a68c-51f17e548725}')
    USER_NAME = 'TESTUSER'
    AGE = 22
    HEIGHT = 169.00
    WEIGHT = 145.00
    BODY_FAT = 0.05
    GOAL = 0

    USER_POST_SUCCESS_MESSAGE = {
        "status": "SUCCESS", 
        "user_id": USER_ID, 
    }

    USER_POST_FAILURE_MESSAGE = {
       'status': "FAILURE" 
    }

    USER_POST_REQUEST = {
        'user_name': USER_NAME,
        'age': AGE,
        "height": HEIGHT,
        "weight": WEIGHT,
        "body_fat": BODY_FAT,
        'goal': GOAL
    }