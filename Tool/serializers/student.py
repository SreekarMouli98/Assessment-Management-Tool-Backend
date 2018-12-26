from rest_framework.serializers import ModelSerializer
from Tool.models import *
from Tool.serializers.user import UserSerializer, UserSignupSerializer

class StudentSerializer(ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Student
        fields = '__all__'

class StudentSignupSerializer(ModelSerializer):
    user = UserSignupSerializer()
    
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'), is_student=True)
        validated_data.pop('optedCourses')
        validated_data.pop('registrations')
        return Student.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        user                   = validated_data.pop('user')
        instance.user.username = user.get('username', instance.user.username)
        instance.user.email    = user.get('email', instance.user.email)
        instance.user.password = user.get('password', instance.user.password)
        instance.college       = validated_data.get('college', instance.college)
        instance.branch        = validated_data.get('branch', instance.branch)
        instance.section       = validated_data.get('section', instance.section)
        instance.optedCourses.set(validated_data.pop('optedCourses'))
        instance.registrations.set(validated_data.pop('registrations'))
        instance.save()
        return instance