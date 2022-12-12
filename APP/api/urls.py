from django.urls import path
# from APP.api.views import movies_list, movies_details
from APP.api.views import WatchListAV, WatchDetailAV,StreamPlatformAV,StreamPlatfromDetailAV
urlpatterns = [
    path('list/', WatchListAV.as_view(),name='movies_list'),
    path('<int:pk>', WatchDetailAV.as_view(),name='movies_detail'),
    path('stream/', StreamPlatformAV.as_view(),name='stream'),
    path('stream/<int:pk>', StreamPlatfromDetailAV.as_view(),name='stream_detail')
]