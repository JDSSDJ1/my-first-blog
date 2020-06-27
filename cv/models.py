from django.db import models
from django.conf import settings

class Section(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    order = models.IntegerField(default=0)

    def publish(self):
        self.save()

    # def __str__(self):
    #     return self.title

# class AllSections(models.Model):
#     theSections = models.Section()

# class Item(models.Model):
#     text = models.TextField(default='')