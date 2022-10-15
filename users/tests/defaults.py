import uuid

class UserDefaults:
    USER_ID = uuid.UUID('{f81ee084-9cef-49cc-a68c-51f17e548725}')
    USER_NAME = 'TESTUSER'
    AGE = 22
    HEIGHT = 169.00
    WEIGHT = 145.00
    BODY_FAT = 0.05
    GOAL = 0

    USER_POST_SUCCESS_MESSAGE = {
        "result": "SUCCESS", 
        "user_id": user_id, 
        'data': result
    }

    USER_POST_FAILURE_MESSAGE = {
        
    }

    USER_POST_REQUEST = {

    }