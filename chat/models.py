from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField("accounts.User", related_name="channels")
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
