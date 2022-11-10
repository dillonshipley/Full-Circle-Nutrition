import uuid

class RecipeDefaults:
    BASE_URL = "/v0/recipes/"
    RECIPE_ID = uuid.UUID('{f81ee084-9cef-49cc-a68c-51f17e548725}')
    RECIPE_NAME = 'TESTRECIPE'
    CREATOR = 'TESTUSER'
    PRICE = 1.01
    MEAL_TYPE = "SK"
    DESCRIPTION = 'TEST DESCRIPTION'

    RECIPE_POST_SUCCESS_MESSAGE = {
        "status": "SUCCESS",
        "recipe_id": RECIPE_ID
    }

    RECIPE_POST_FAILURE_MESSAGE = {
        "status": "FAILURE"
    }

    RECIPE_POST_REQUEST = {
        "recipe_name": RECIPE_NAME,
        "creator": CREATOR,
        "price": PRICE,
        "meal_type": MEAL_TYPE,
        "description": DESCRIPTION
    }