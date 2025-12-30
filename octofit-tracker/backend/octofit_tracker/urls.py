
import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracker import views
from django.http import JsonResponse

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include(router.urls)),
	# Custom API root that returns the correct API base URL using $CODESPACE_NAME
	path('', lambda request: JsonResponse({
		"api_base_url": f"https://{os.environ.get('CODESPACE_NAME', 'localhost')}-8000.app.github.dev/api/"
	}), name='api-root'),
]
