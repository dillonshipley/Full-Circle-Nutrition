import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.timezone import now


class UserManager(models.Manager):
    def create_user(
        self,
        user_name: str,
        age: int,
        height: float,
        weight: float,
        body_fat: float,
        goal: int,
    ) -> uuid:
        """Creates and validates new user entries to the database. Returns the UUID of the new user

        Args:
            user_name (str): _description_
            age (int): _description_
            height (float): _description_
            weight (float): _description_
            body_fat (float): _description_
            goal (int): _description_
        Returns:
            uuid: _description_
        """
        self.create(
            user_name=user_name,
            age=age,
            height=height,
            weight=weight,
            body_fat=body_fat,
            goal=goal,
        ).clean()
        return self.last().user_id

    def get_user_by_id(self, user_id: uuid):    
        try:
            return self.get(user_id=user_id)
        except ObjectDoesNotExist:
            return None

    def delete_user_by_id(self, user_id: uuid) -> bool:
        try:
            user_to_delete = self.get(user_id=user_id)
            user_to_delete.delete()
            return True
        except ObjectDoesNotExist:
            return False

class User(models.Model):
    goal_choices = (
        ("-3", "Very rapid loss"),
        ("-2", "Rapid loss"),
        ("-1", "Moderate loss"),
        ("0", "Maintain"),
        ("1", "Moderate gain"),
        ("2", "Rapid gain"),
        ("3", "Very rapid gain"),
    )

    user_id = models.UUIDField(
        name="user_id",
        primary_key=True,
        max_length=36,
        null=False,
        unique=True,
        editable=False,
        default=uuid.uuid4(),
    )
    user_name = models.CharField(name="user_name", max_length=25, unique=True)
    age = models.IntegerField(name="age", null=False, default=25)
    height = models.DecimalField(
        name="height", decimal_places=2, null=False, max_digits=8, default=0.00
    )
    weight = models.DecimalField(
        name="weight", decimal_places=2, null=False, max_digits=8, default=0.00
    )
    body_fat = models.DecimalField(
        name="body_fat", decimal_places=2, null=False, max_digits=8, default=0.00
    )
    goal = models.CharField(
        name="goal", choices=goal_choices, max_length=2, null=False, default="0"
    )
    create_date = models.DateTimeField(name="create_date", editable=False, default=now)
    modify_date = models.DateTimeField(name="modify_date", default=now)

    objects = UserManager()

    @property
    def id(self) -> uuid:
        return self.user_id

    def serialize(self) -> dict:
        """Serialize the User model into a JSON(ish) response. Replaces the default Django serializer since it can't
        handle datetimes properly

        Returns:
            dict: Serialized User object
        """
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "age": self.age,
            "height": float(self.height),
            "weight": float(self.weight),
            "goal": self.get_goal_display(),
            "create_date": self.create_date,
            "modify_date": self.modify_date,
        }

    def __str__(self) -> str:
        return f"User({self.user_name}): {self.user_id}"
