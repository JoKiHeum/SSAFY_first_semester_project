"""
URL configuration for final_pjt_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),                          # 게시판
    path('finances/', include('finances.urls')),                          # 금융 상품 관련
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),  # 회원생성
    path('user/', include('accounts.urls')),                              # 회원 관련
    path('accounts/', include('dj_rest_auth.urls')),                      # 로그인 및 로그아웃
    path("finances/", include("finances.urls")),                          # 금융 상품 관련
    path("chatbot/", include("chatbot.urls")),                            # 챗봇
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
