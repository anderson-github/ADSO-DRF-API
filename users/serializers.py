from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    birthDate = serializers.DateField(source="birth_date")
    biography = serializers.CharField(required=False)

    class Meta:
        abstract = True


class OutputSerializer(InputSerializer):
    password = None
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")


class LogInInputSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)


class LogInOutputSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")


class ProfileOutputSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    birthDate = serializers.DateField(source="birth_date")
    biography = serializers.CharField(required=False)

