from django.db import models
import uuid


class BaseModel(models.Model):
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_name = models.CharField(max_length=100)


class Question(BaseModel):
    category = models.ForeignKey(
        Category, related_name='categoy', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)


class Anwser(BaseModel):
    question = models.ForeignKey(
        Question, related_name='question_answer', on_delete=models.CASCADE)
    anwser = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
