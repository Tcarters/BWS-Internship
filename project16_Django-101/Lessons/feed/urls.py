from unicodedata import name
from django.urls import path
from .views import HomePageView, PostDetailView

app_name ='feed'

urlpatterns =[
    path('', HomePageView.as_view(), name='index' ),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    
    # <int:pk> means whenever you see an endpoint integer replace it by pk (pk =Primary Key)
]

