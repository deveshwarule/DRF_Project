from django.urls import path, include
# from APP.api.views import movies_list, movies_details
from APP.api.views import (WatchListAV, WatchDetailAV,StreamPlatformAV,StreamPlatfromDetailAV, StreamPlatformVS,
                           ReviewList,ReviewDetail,ReviewCreate)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(),name='movies_list'),
    path('<int:pk>', WatchDetailAV.as_view(),name='movies_detail'),
    path('',include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(),name='stream'),
    # path('stream/<int:pk>', StreamPlatfromDetailAV.as_view(),name='stream_detail'),
    
    # path('review/', ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(),name='stream-detail'),
    
    path('<int:pk>/review-create', ReviewCreate.as_view(),name='Review-create'),
    path('<int:pk>/reviews', ReviewList.as_view(),name='Review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(),name='review-detail'),
    
]