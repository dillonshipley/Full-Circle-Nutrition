import logging
from django.http import QueryDict
from django.core.exceptions import ValidationError

log = logging.getLogger("ingredients")

class GetByFiltersValidator:
    PREFIX = "filter"
    SEPERATOR = ","

    def validate(query_params: QueryDict) -> tuple:
        """Validate provided query params for the ingredient get by filters endpoint

        Args:
            query_params (QueryDict): _description_
        Returns:
            tuple: _description_
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