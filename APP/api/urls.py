from django.urls import path
# from APP.api.views import movies_list, movies_details
from APP.api.views import (WatchListAV, WatchDetailAV,StreamPlatformAV,StreamPlatfromDetailAV, 
                           ReviewList,ReviewDetail)
urlpatterns = [
    path('list/', WatchListAV.as_view(),name='movies_list'),
    path('<int:pk>', WatchDetailAV.as_view(),name='movies_detail'),
    path('stream/', StreamPlatformAV.as_view(),name='stream'),
    path('stream/<int:pk>', StreamPlatfromDetailAV.as_view(),name='stream_detail'),
    
    path('review/', ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(),name='stream-detail'),
    
    # path('stream/<int:pk>/review', StreamPlatfromDetailAV.as_view(),name='stream_detail'),
    # path('stream/review/<int:pk>', ReviewList.as_view(),name='review-list'),
    
]