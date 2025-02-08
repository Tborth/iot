# models.py in RAG_Chatbot app
from django.db import models
import os


class RuleModel(models.Model):
    rule_name = models.TextField()
    sensor_id = models.TextField(null = True,blank = True)
    field_name = models.TextField(null = True,blank = True)
    condition = models.TextField(null = True,blank = True)
    thrashold =  models.TextField(null = True,blank = True)
    duration = models.IntegerField(null = True,blank = True)
    status = models.CharField(null = True,blank = True,max_length=20)


    def __str__(self):
        return f"{self.sensor_id}"
    

##############################################################################

class AlertName(models.Model):
    type =models.TextField(null = True)
    rule_name=models.TextField(null = True)
    sensor_id=models.TextField(null = True)
    content=models.TextField(null = True,blank = True)

    def __str__(self):
        return f"{self.sensor_id}"