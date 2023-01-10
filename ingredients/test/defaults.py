import uuid


class IngredientDefaults:
    BASE_URL = "/v0/ingredients/"
    INGREDIENT_ID = uuid.UUID("{f81ee084-9cef-49cc-a68c-51f17e548725}")
    NAME = "TESTINGREDIENT"
    VEGETARIAN = False
    GLUTEN_FREE = False
    CALORIES = 100
    FAT = 10
    PROTEIN = 10
    UNITS = "TBP"
    UNITS_VERBOSE = "table spoon"

    INGREDIENT_POST_REQUEST = {
        "name": NAME,
        "vegetarian": VEGETARIAN,
        "gluten_free": GLUTEN_FREE,
        "calories": CALORIES,
        "fat": FAT,
        "protein": PROTEIN,
        "units": UNITS,
    }

    INGREDIENT_POST_SUCCESS_MESSAGE = {
        "status": "SUCCESS",
        "status_code": 201,
        "ingredient_id": INGREDIENT_ID,
    }

    INGREDIENT_POST_FAILURE_MESSAGE = {"status": "FAILURE", "status_code": 400}

    INGREDIENT_GET_SUCCESS_MESSAGE = {
        "status": "SUCCESS",
        "status_code": 200,
        "ingredient": {
            "name": NAME,
            "vegetarian": VEGETARIAN,
            "gluten_free": GLUTEN_FREE,
            "calories": CALORIES,
            "fat": FAT,
            "protein": PROTEIN,
            "units": UNITS_VERBOSE,
        },
    }

    INGREDIENT_PATCH_REQUEST = {"fat": 12}

    INGREDIENT_DELETE_SUCCESS_MESSAGE = {"status": "SUCCESS", "status_code": 200}
