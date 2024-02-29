from todo_api.models import User, TaskList, Task
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'firstName', 'email', 'hash'] 
        
class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ['id' ,'name']
        
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'state', 'body', 'taskList_id']
        



