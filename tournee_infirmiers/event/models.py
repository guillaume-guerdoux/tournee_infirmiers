from django.db import models


class Need(models.Model):
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
