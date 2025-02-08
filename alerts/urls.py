from django.urls import path
# from .views import upload_query_view,vectorstore_view,upload_view
from .views import env_variable_view,delete_env_variable,update_env_variable,all_alerts

urlpatterns = [
   
    path('env_variable', env_variable_view, name='env_variable_form'),
    path('delete-env-variable/<int:id>/',delete_env_variable, name='delete_env_variable'),
    path('update_env_variable/<int:id>/',update_env_variable, name='update_env_variable'),
    # path('all_alerts', all_alerts, name='all_alerts'),
    path('all_alerts/', all_alerts, name='all_alerts'),
]

