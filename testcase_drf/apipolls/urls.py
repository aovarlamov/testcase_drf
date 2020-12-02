from django.contrib import admin
from django.urls import path, include
from  . import views

urlpatterns = [
    # path('', include('rest_framework.urls')),
    path('login/', views.Login.as_view()),
    path('poll/view/', views.PollListView.as_view()),
    path('poll/view/active/', views.PollListViewActive.as_view()),
    path('poll/create/', views.PollCreate.as_view()),
    path('poll/update/<int:poll_id>', views.PollUpdate.as_view()),
    path('poll/delete/<int:poll_id>', views.PollDelete.as_view()),
    path('question/create/', views.QuestionCreate.as_view()),
    path('question/update/<int:question_id>', views.QuestionUpdate.as_view()),
    path('question/delete/<int:question_id>', views.QuestionDelete.as_view()),
    path('choice/create/', views.ChoiceCreate.as_view()),
    path('choice/update/<int:choice_id>', views.ChoiceUpdate.as_view()),
    path('choice/delete/<int:choice_id>', views.ChoiceDelete.as_view()),
    path('answer/create/', views.AnswerCreate.as_view()),
    path('answer/update/<int:answer_id>', views.AnswerUpdate.as_view()),
    path('answer/delete/<int:answer_id>', views.AnswerDelete.as_view()),
    path('answer/view/<int:user_id>', views.AnswerView.as_view()),
]
