from django.urls import path
from . import views

urlpatterns = [
    # path('', views.start, name='start'),
    # path('test', views.test, name='test'),
    # path('testc', views.insert_into_actionhistory_question_id, name='insert_into_actionhistory_question_id'),
    path('test/<int:id>/', views.test),
    # path('generate', views.generate_link, name='generate'),
    # path('test/<int:id>/check_test', views.check_test, name='check_test'),

]
