from django.db import models
from django.utils import timezone
import shortuuid

# Create your models here.
class Notebook(models.Model):
	bookname = models.CharField(max_length=200)
	note = models.TextField()
	title = models.CharField(max_length=200)
	noteid = models.CharField(max_length=200)
	created_date = models.DateField(default=timezone.now)

