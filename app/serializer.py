from rest_framework import serializers
from app.models import todo


# serializers => this is used from converting  data into JSON format and vice versa

class todoserializer(serializers.ModelSerializer):
    class Meta():
        model = todo
        fields = "__all__"