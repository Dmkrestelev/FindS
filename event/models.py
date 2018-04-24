from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(null=True)
    creator_id = models.IntegerField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    participants = models.IntegerField(null=True)
    class Meta:
        ordering = ["-id"]