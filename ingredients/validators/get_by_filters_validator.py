from django.http import QueryDict

class GetByFiltersValidator:
    PREFIX = "filter"
    SEPERATOR = ","

    def validate(query_params: QueryDict) -> bool:
        return True