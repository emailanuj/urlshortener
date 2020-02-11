from django.db import models

# Create your models here.
class short_urls(models.Model):
    short_url=models.CharField(max_length=200,blank=True,null=True,default='')
    long_url=models.URLField("URL",unique=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    class Meta:
        verbose_name=('Short URL')
        verbose_name_plural=('Short URLs')
    def __str__(self):
        return self.long_url