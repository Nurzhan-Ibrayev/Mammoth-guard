from django.db import models
from django.contrib.auth.models import User, Permission, ContentType

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(User, related_name='courses_enrolled', blank=True)  # Many-to-many with User
    teachers = models.ManyToManyField('Teacher', related_name='courses_taught', blank=True)  # Many-to-many with Teachers

    
   
class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    sequence = models.IntegerField()

    class Meta:
        unique_together = ('course', 'sequence')

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    can_become_teacher = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.can_become_teacher: 
            content_type = ContentType.objects.get_for_model(self)
            permission, _ = Permission.objects.get_or_create(
                codename='can_become_teacher',
                name='Can become teacher',
                content_type=content_type
            )
            self.user.user_permissions.add(permission)
        else:
            # Remove 'can_become_teacher' permission from the user
            permission = Permission.objects.filter(codename='can_become_teacher').first()
            if permission:
                self.user.user_permissions.remove(permission)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.user.username
    


    

