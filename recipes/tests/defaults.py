import uuid


class RecipeDefaults:
    BASE_URL = "/v0/recipes/"
    RECIPE_ID = uuid.UUID("{f81ee084-9cef-49cc-a68c-51f17e548725}")
    RECIPE_NAME = "TESTRECIPE"
    CREATOR = "TESTUSER"
    PRICE = 1.01
    MEAL_TYPE = "SK"
    MEAL_TYPE_VERBOSE = "Snack"
    DESCRIPTION = "TEST DESCRIPTION"

    RECIPE_POST_SUCCESS_MESSAGE = {
        "status": "SUCCESS",
        "status_code": 201,
    }

    RECIPE_POST_FAILURE_MESSAGE = {"status": "FAILURE"}

    RECIPE_POST_REQUEST = {
        "recipe_name": RECIPE_NAME,
        "creator": CREATOR,
        "price": PRICE,
        "meal_type": MEAL_TYPE,
        "description": DESCRIPTION,
    }

    RECIPE_PATCH_REQUEST = {"meal_type": "DN"}

    RECIPE_GET_SUCCESS_MESSAGE = {
        "status": "SUCCESS",
        "status_code": 200,
        "recipe": {
            "recipe_name": RECIPE_NAME,
            "creator": CREATOR,
            "price": PRICE,
            "meal_type": MEAL_TYPE_VERBOSE,
            "description": DESCRIPTION,
        },
    }

    RECIPE_DELETE_SUCCESS_MESSAGE = {"status": "SUCCESS", "status_code": 200}
