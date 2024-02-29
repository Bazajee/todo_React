from django.db import models


class User (models.Model):
    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    hash = models.CharField(max_length=150)
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.firstName}"
    
    
class TaskList (models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
    
    
class Task(models.Model):
    state = models.BooleanField()
    body = models.CharField(max_length=50)
    taskList_id = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.body}"





