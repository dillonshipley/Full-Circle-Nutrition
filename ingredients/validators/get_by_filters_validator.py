import logging
from django.http import QueryDict
from django.core.exceptions import ValidationError, FieldError

log = logging.getLogger("ingredients")

class GetByFiltersValidator:
    PREFIX = "filter"
    SEPERATOR = ","

    # TODO: Finish getByFilters validator class and cases
    def validate(query_params: QueryDict) -> tuple:
        """Validate provided query params for the ingredient get by filters endpoint

        Args:
            query_params (QueryDict): Query parameters provided to the endpoint by the client
        Returns:
            tuple(bool, [dict | ValidationError]): Tuple containing the result of the operation
            and 
        """        
        filter_values = dict(
            zip(
                [key.removeprefix("filter.") for key in query_params],
                query_params.dict().values(),
            )
        )
        
        if len(filter_values) == 0:
            return False, ValidationError("No filters provided")

        # Field error if any of the keys do not match the expected keys
        
        log.debug(filter_values)
        return True, filter_values