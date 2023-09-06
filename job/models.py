from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time' , 'Full Time'),
    ('Part time' , 'Part time'),
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=500)
    publish_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
