from django.db import models
from category.models import category

class post (models.Model) :
    id_post = models.AutoField(primary_key=True)
    id_category = models.ForeignKey(category, related_name='idcategory', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()
    
    def __str__(self) :
        return "{}".format(self.title)
