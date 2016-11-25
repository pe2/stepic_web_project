from django.db import models
from django.contrib.auth.models import User
from django.db import connection
from django.shortcuts import render

# Create your models here.
class QuestionManager(models.Manager):
	def new(self, page):
#		body = "test > " + page + " op op"	
#		cur = connection.cursor()
#		cur.execute("select * from qa_question");
#		for question in cur.fetchall():
#			text, rating = question
		questions = Question.objects.all()
		questions.filter(id__gt=10)	
		return render(self, 'qa/index.html', { 'page' : page, })
	
	def popular():
		pass

class Question(models.Model):
	objects = QuestionManager()
	title=models.CharField(max_length=255)
	text=models.TextField()
	added_at=models.DateField(blank=True, auto_now_add=True)
	rating=models.IntegerField(default=0)
	author=models.ForeignKey(User)
	#author=models.OneToOneField(User)
	likes=models.ManyToManyField(User, related_name="likes_set")

class Answer(models.Model):
	text=models.TextField()
	added_at=models.DateField(blank=True, auto_now_add=True)
	question=models.ForeignKey(Question)
	#question=models.OneToOneField(Question)
	#author=models.OneToOneField(User)
	author=models.ForeignKey(User)
