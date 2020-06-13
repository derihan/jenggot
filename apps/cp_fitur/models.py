from django.db import models

class Fitur(models.Model):
    
    fitur_name = models.CharField(max_length=50)
    fitur_url = models.CharField(max_length=50)
    fitur_created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'apps_fitur0'
        managed = True
# Create your models here.
