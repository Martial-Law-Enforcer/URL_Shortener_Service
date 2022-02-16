from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import URL_Mapping
import random
import string

# Create your views here.

# Shorten a full URL
class URL_Shorten_View(APIView):
	def post(self, request, format=None):
		original_url = request.data.get('url')
		
		# Validates that the original URL is supplied in the request body
		if not original_url:
			return Response({'success': False, 'message': 'URL is required'}, status=400)
		
		# If the original URL is already shortened, returns the mapped shortened URL
		if len(URL_Mapping.objects.filter(original_url=original_url)) > 0:
			url_id = URL_Mapping.objects.filter(original_url=original_url)[0].url_id
			return Response({'success': True, 'generated_url': request.build_absolute_uri('/') + url_id}, status=200)
			
		else:
			# Otherwise, generates an ID to be used for the shortened URL
			url_id = generate_id()
			
			# To confirmed that the url_id is not mapped previously
			while len(URL_Mapping.objects.filter(url_id=url_id)) > 0:
				url_id = generate_id()
			
			# Creates the mapping and returns the shortened URL
			URL_Mapping.objects.create(url_id=url_id, original_url=original_url)
			return Response({'success': True, 'generated_url': request.build_absolute_uri('/') + url_id}, status=200)


# Redirect a shortened URL to the original URL
class URL_Redirect_View(RedirectView):
	def get_redirect_url(self, *args, **kwargs):
	
		# Get the 8 alphanumeric character ID from the URL
		# Looks for the original URL mapped to the URL ID and redirect to it, otherwse returns 404
		url_mapping = get_object_or_404(URL_Mapping, url_id=kwargs['url_id'])
		return url_mapping.original_url
		

# Generate a random 8 alphanumeric character ID
def generate_id():
	id_charset = string.ascii_letters + string.digits
	return "".join([str(random.choice(id_charset)) for _ in range(8)])