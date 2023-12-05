from rest_framework import serializers
from Smsapi.models import Students,Enrolments,Courses

class StudentEnrolSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=Enrolments
        fields="__all__"
    

class StudentSerializer(serializers.ModelSerializer):
        avg_mark=serializers.CharField(read_only=True)

        class Meta:
             model=Students
             fields="__all__"


class CourseSerializer(serializers.ModelSerializer):
        class Meta:
             model=Courses
             fields="__all__"







