import uuid

from django.db import models
from django.utils.timezone import now


class UserManager(models.Manager):
    def user_count(self, keyword) -> int:
        return self.filter(user_id_icontain=keyword).count()


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
        verbose_name="user model unique identifier",
        max_length=36,
        primary_key=True,
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
    create_date = models.DateTimeField(name="create_date", default=now)
    modify_date = models.DateTimeField(name="modify_date", default=now)

    objects = UserManager()

    @property
    def id(self) -> uuid:
        return self.user_id

    def describe(self) -> str:
        pass

    def to_dict(self) -> dict:
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
