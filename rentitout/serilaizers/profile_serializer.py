from rest_framework import serializers

from rentitout.models import User


class ProfileSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    def get_role(self, obj):
        if not obj:
            return None
        if obj.role == 1:
            return 'CLIENT'
        elif obj.role == 2:
            return 'DONER'
        elif obj.role == 3:
            return 'VOLUNTEER'
        else:
            return 'ADMIN'

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email',
            'username', 'role'
        ]
