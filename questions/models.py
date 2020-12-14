from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=75)
    questions = models.ForeignKey('Question', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.name


class Date(models.Model):
    month = models.CharField("mes", max_length=10)
    year = models.IntegerField("año", )
    model = models.CharField("modelo", max_length=100)

    def __str__(self):
        return f'{self.month}-{self.year}/{self.model}'


class Question(models.Model):
    text = models.CharField("text", max_length=250)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    responses = models.JSONField()

    def __str__(self):
        return self.text
