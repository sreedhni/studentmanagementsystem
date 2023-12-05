from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    student_id=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    def avg_mark(self):
        mark=self.enrolments_set.all().values_list("mark",flat=True)
        return sum(mark)/len(mark) if mark else 0



    def __str__(self):
        return self.student_id

class Courses(models.Model):

    name=models.ForeignKey(Students,on_delete=models.CASCADE,null=True)
    course_code=models.CharField(max_length=100)
    credithours=models.CharField(max_length=100)

    def __str__(self):
        return self.name.name
    
class Enrolments(models.Model):
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    enrolment_date=models.DateTimeField(auto_now_add=True,null=True)
    mark=models.PositiveIntegerField(null=True)
    
    






