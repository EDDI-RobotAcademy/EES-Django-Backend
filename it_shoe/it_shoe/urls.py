from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/', include('review.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('kakao_oauth/', include('kakao_oauth.urls')),
    path('account/', include('account.urls')),
    path('community/', include('community.urls')),
    path("view-count/", include('viewCount.urls')),
]