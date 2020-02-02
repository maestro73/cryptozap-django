from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


class Scan(models.Model):

    
    


  

    def print_hello():

        return "hello there pirate"

