from django.db import models

class Package(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField()
    image       = models.TextField()
    pax         = models.IntegerField()
    venue       = models.CharField(max_length=255)
    price       = models.TextField(max_length=50)
    timestamps  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)