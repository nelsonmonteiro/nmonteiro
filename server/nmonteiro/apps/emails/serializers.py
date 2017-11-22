from rest_framework import serializers
from apps.users.mixins import UserPermissionSerializerMixin
from .models import Device, DeviceVariable, DeviceMethod, DeviceMethodParam, DeviceEvent, DeviceEventParam


# -----------------------------------------------------------------------------
# EVENTS
# -----------------------------------------------------------------------------
class DeviceEventParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceEventParam
        fields = ['id', 'name', 'description', 'param_type']


class DeviceEventSerializer(serializers.ModelSerializer):
    params = DeviceEventParamSerializer(many=True)

    class Meta:
        model = DeviceEvent
        fields = ['id', 'name', 'description', 'params']


# -----------------------------------------------------------------------------
# METHODS
# -----------------------------------------------------------------------------
class DeviceInfoSerializer(UserPermissionSerializerMixin):
    class Meta:
        model = Device
        fields = ['id', 'name']


class DeviceMethodParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceMethodParam
        fields = ['id', 'name', 'description', 'param_type', 'required']


class DeviceMethodSerializer(serializers.ModelSerializer):
    params = DeviceMethodParamSerializer(many=True)
    device = DeviceInfoSerializer()

    class Meta:
        model = DeviceMethod
        fields = ['id', 'name', 'description', 'device', 'params']


# -----------------------------------------------------------------------------
# DEVICE
# -----------------------------------------------------------------------------
class DeviceVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceVariable
        fields = ['id', 'name', 'description']


class DeviceVariableInfoSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(source='device', slug_field='name', read_only=True)

    class Meta:
        model = DeviceVariable
        fields = ['id', 'name', 'parent']


class DeviceSerializer(UserPermissionSerializerMixin):
    variables = DeviceVariableSerializer(many=True)

    class Meta:
        model = Device
        fields = ['id', 'name', 'broadcast', 'bluetooth', 'permissions',
                  'visibility', 'visibility_display', 'no_request_needed_to_join']


class DeviceListSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Device
        fields = ['id', 'name', 'owner']

    def get_owner(self, obj):
        owner = obj.owner
        return owner.get_full_name() if owner else None


# -----------------------------------------------------------------------------
# DEVICE SETUP
# -----------------------------------------------------------------------------
class DeviceTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'token']


class DeviceVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'specifications_version']


