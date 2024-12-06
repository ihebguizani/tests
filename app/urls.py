
from django.urls import path, include
from .views import RegisterView, UtilisateurViewSet, DocumentViewSet, LoginView, RefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', RefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]