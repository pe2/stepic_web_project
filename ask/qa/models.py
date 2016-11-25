from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
	def new(self, page):
		body = "test123" + page + " op op"	
		return body
	
	def popular():
		pass

class Question(models.Model):
	objects = QuestionManager()
	title=models.CharField(max_length=255)
	text=models.TextField()
	added_at=models.DateField(blank=True, auto_now_add=True)
	rating=models.IntegerField(default=0)
	#author=models.ForeignKey(User)
	author=models.OneToOneField(User)
	likes=models.ManyToManyField(User, related_name="likes_set")

class Answer(models.Model):
	text=models.TextField()
	added_at=models.DateField(blank=True, auto_now_add=True)
	#question=models.ForeignKey(Question, unique=True)
	question=models.OneToOneField(Question)
	#author=models.OneToOneField(User)
	author=models.ForeignKey(User)
