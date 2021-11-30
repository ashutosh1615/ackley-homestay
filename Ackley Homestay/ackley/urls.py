from django.urls import path
from . import views
app_name='ackley'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /ackley/5/results/
    # path('results/', views.ResultsView.as_view(), name='results'),
    # ex: /ackley/5/vote/
    # path('vote/', views.vote, name='vote'),
    path('Contact us/',views.contact,name='contact'),
    path('Photo/',views.photo,name='photo'),
    path('reviews/',views.review,name='reviews'),
    path('booking/',views.online_booking,name='booking'),
]