from django.urls import path, include
from main.views import *
from rest_framework.routers import DefaultRouter

def trigger_error(request):
    division_by_zero = 1 / 0

router=DefaultRouter()
router.register('post', PostViewSet)
router.register('type', TypeViewSet)

urlpatterns=[
    path('api/', include(router.urls)),
    path('sentry-debug/', trigger_error), #sentry
]