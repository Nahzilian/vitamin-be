from rest_framework import routers
from .api import GuestViewSet

router = routers.DefaultRouter()
router.register('api/guest',GuestViewSet,'guest')

urlpatterns = router.urls