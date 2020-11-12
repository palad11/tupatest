from django.db import models


# Create your models here.


class Answer(models.Model):
    description = models.TextField()


class Question(models.Model):
    description = models.TextField()
    answers = models.ManyToManyField(Answer)


class Opros(models.Model):
    opros = models.ManyToManyField(Question)
