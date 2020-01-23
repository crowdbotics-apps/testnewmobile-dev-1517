from rest_framework import serializers
from users.models import Tester


class TesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tester
        fields = "__all__"
