from httptest2.testmodule.models import TestModule

from rest_framework import serializers


class TestDeliverySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    delivery_id = serializers.IntegerField()
    status = serializers.BooleanField()

    def create(self, validated_data):
        return TestModule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.testmodule_id = validated_data.get('testmodule_id', instance.testmodule_id)
        instance.status = validated_data.get('status', instance.status)
