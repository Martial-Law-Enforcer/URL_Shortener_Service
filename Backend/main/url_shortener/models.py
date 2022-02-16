from django.db import models
from django.core.validators import URLValidator

# Create your models here.

# To validate the URL
url_validator = URLValidator(schemes=["http", "https"])

# Model Definition for URL_Mapping
class URL_Mapping(models.Model):
	
	# A 8 alphanumeric character ID that will be mapped to the original URL
	# e.g. If a1b2c3d4 is the generated ID, then the shortened URL will be https://<host>/a1b2c3d4
	url_id = models.CharField(max_length=8, unique=True, primary_key=True)
	
	# Full URL that will be shortened
	original_url = models.URLField(max_length=100, unique=True, validators=[url_validator])
	
	class Meta:
		db_table = 'url_mapping'
		verbose_name = 'URL Mapping'
		indexes = [models.Index(fields=['url_id']), ]