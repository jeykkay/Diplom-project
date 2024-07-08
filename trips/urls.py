from django.urls import path
from rest_framework.routers import DefaultRouter

from trips.views import (CarViewSet, TripViewSet,
                         BookingAPIView, RatingAPIView,
                         CommentAPIView, RatingDetailAPIView, CommentDetailAPIView)


router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')
router.register(r'trips', TripViewSet, basename='trips')


urlpatterns = [
    path('create-booking/', BookingAPIView.as_view(), name='create-booking'),

    path('add-rating/', RatingAPIView.as_view(), name='add-rating'),
    path('add-rating/<int:driver_id>/', RatingDetailAPIView.as_view()),

    path('add-comment/', CommentAPIView.as_view(), name='add-comment'),
    path('add-comment/<int:pk>/', CommentDetailAPIView.as_view())
]

urlpatterns += router.urls
