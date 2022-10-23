from os import set_inheritable
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "user_id",
            "user_name",
            "age",
            "height",
            "weight",
            "body_fat",
            "goal",
            "create_date",
            "modify_date",
        )

class PatchRequestSerializer