from django.urls import path, re_path
import url_shortener.views as views

urlpatterns = [
    path('shorten', views.URL_Shorten_View.as_view(), name='api_shorten'),
	re_path(r'(?P<url_id>^[A-Za-z0-9]{8}$)', views.URL_Redirect_View.as_view(), name='api_redirect')
]