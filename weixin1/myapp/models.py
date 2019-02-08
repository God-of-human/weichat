from django.db import models

# Create your models here.
class Grade(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    # def _str_(self):
    #     return self.gname

class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("grade",on_delete=models.DO_NOTHING)
    # def _str_(self):
    #     return self.sname