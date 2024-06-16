from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/', include('review.urls')),
    path('product/', include('product.urls')),
    path('kakao_oauth/', include('kakao_oauth.urls')),
]