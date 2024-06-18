from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kakao_oauth.controller.views import OauthView

router = DefaultRouter()
router.register(r'kakao_oauth', OauthView, basename='kakao_oauth')

urlpatterns = [
    path('', include(router.urls)),
    path('kakao', OauthView.as_view({'get': 'kakaoOauthURI'}), name='get-kakao-oauth-uri'),
    path('kakao/access-token', OauthView.as_view({'post': 'kakaoAccessTokenURI'}), name='get-kakao-access-token-uri'),
    path('kakao/user-info', OauthView.as_view({'post': 'kakaoUserInfoURI'}),
                                name='get-kakao-user-info-uri'),
]