from django.db import models

# Create your models here.
class post (models.Model) :
    id_post = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self) :
        return "{}".format(self.title)
