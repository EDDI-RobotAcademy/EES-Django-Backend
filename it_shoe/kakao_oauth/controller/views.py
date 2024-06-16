from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response

from kakao_oauth.serializer.kakao_oauth_access_token_serializer import KakaoOauthAccessTokenSerializer
from kakao_oauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer
from kakao_oauth.service.oauth_service_impl import OauthServiceImpl


class OauthView(viewsets.ViewSet):
    oauthService = OauthServiceImpl.getInstance()

    def kakaoOauthURI(self, request):
            url = self.oauthService.kakaoLoginAddress()
            print(f"url:", url)
            serializer = KakaoOauthUrlSerializer(data={ 'url': url })
            serializer.is_valid(raise_exception=True)
            print(f"validated_data: {serializer.validated_data}")
            return Response(serializer.validated_data)

    # def kakaoAccessTokenURI(self, request):
    #     serializer = KakaoOauthAccessTokenSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     code = serializer.validated_data['code']
    #
    #     try:
    #         accessToken = self.oauthService.requestAccessToken(code)
    #         print(f"accessToken: {accessToken}")
    #         return JsonResponse({'accessToken': accessToken})
    #     except Exception as e:
    #         return JsonResponse({'error': str(e)}, status=500)