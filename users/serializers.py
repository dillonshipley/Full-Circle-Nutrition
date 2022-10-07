from rest_framework.serializers import ModelSerializer
from users.models import User


class UserSerializer(ModelSerializer):
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
