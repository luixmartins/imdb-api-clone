from django.urls import path 

from media.views import MediaCreateList, MediaDetailUpdateDelete

urlpatterns = [
    path('media/', MediaCreateList.as_view()),
    path('media/<int:pk>/', MediaDetailUpdateDelete.as_view()),
]