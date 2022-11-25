from uuid import UUID, uuid4

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Manager
from django.db.utils import IntegrityError

from .models import User


class UserManager(Manager):
    def create_user(
        self,
        user_name: str,
        age: int,
        height: float,
        weight: float,
        body_fat: float,
        goal: int,
    ) -> tuple:
        """Creates and validates new user entries to the database. Returns the UUID of the
        new user

        Args:
            user_name (str): User name of the new object
            age (int): Age of the new user
            height (float): Height of the new user
            weight (float): Weight of the new user
            body_fat (float): Body fat percentage of the new user
            goal (int): Starting goal of the new user
        Returns:
            tuple: Result of the operation and the UUID of the new user, or an error message
        """
        try:
            self.create(
                user_id=uuid4(),
                user_name=user_name,
                age=age,
                height=height,
                weight=weight,
                body_fat=body_fat,
                goal=goal,
            ).clean()
            return True, self.last().user_id
        except IntegrityError as e:
            return False, e

    def get_user_by_id(self, user_id: UUID) -> tuple:
        """Retrieve an user using the user_id as a query

        Args:
            user_id (UUID): User id of the User model that should be restored
        Returns:
            tuple(bool, [User, Error]): Tuple containing the success of the operation,
            and the resulting User or error
        """
        try:
            return True, self.get(user_id=user_id)
        except ObjectDoesNotExist as e:
            return False, e

    def delete_user_by_id(self, user_id: UUID) -> bool:
        """Remove a user from the db using the user_id as a query

        Args:
            user_id (UUID): UUID of the user that should be deleted
        Returns:
            bool: True if the object was successfully removed from the db, False otherwise
        """
        try:
            user_to_delete = self.get(user_id=user_id)
            user_to_delete.delete()
            return True
        except ObjectDoesNotExist:
            return False
