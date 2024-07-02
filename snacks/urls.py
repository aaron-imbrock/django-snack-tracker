from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='snack_list'),
    #path('snack_list', SnackListPageView.as_view(), name='snack_list')
]
