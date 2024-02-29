from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from django.contrib import admin
from todo_api.views import allLists, allTasks

#router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lists/', allLists.as_view()), 
    path('api/tasks/', allTasks.as_view()), 
]


#urlpatterns += router.urls