from rest_framework import viewsets
from rest_framework.response import Response

from oauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer
from oauth.service.oauth_service_impl import OauthServiceImpl


class OauthView(viewsets.ViewSet):
    oauthService = OauthServiceImpl.getInstance()

    def kakaoOauthURI(self, request):
            url = self.oauthService.kakaoLoginAddress()
            print(f"url:", url)
            serializer = KakaoOauthUrlSerializer(data={ 'url': url })
            serializer.is_valid(raise_exception=True)
            print(f"validated_data: {serializer.validated_data}")
            return Response(serializer.validated_data)