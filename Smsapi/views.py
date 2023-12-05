from django.shortcuts import render
from Smsapi.serializers import StudentEnrolSerializer,StudentSerializer,CourseSerializer
from Smsapi.models import Students,Courses,Enrolments

from rest_framework.viewsets import ModelViewSet

# Create your views here.

class StudentEnrolmentView(ModelViewSet):
    queryset=Enrolments.objects.all()
    serializer_class=StudentEnrolSerializer

    def avg_mark(self):
        total_mark=sum(self.mark)
        total=len(self.mark)
        avg_mark=total_mark/total
        return self.avg_mark

class StudentAddView(ModelViewSet):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer

class CourseView(ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializer



    
    



