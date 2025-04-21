from django.db import models

# Create your models here.
class Candidates(models.Model):
    cand_name = models.CharField(max_length = 50)
    cand_class = models.CharField(max_length = 50)
    cand_adm = models.CharField(max_length = 50)
    cand_division = models.CharField(max_length = 100)
    cand_post = models.CharField(max_length = 100)
    pic = models.ImageField(upload_to = 'candidates/')
     

    class Meta:
        db_table = "candidates"

class Votes(models.Model):
    candidates = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    votes = models.IntegerField()
     
     

    class Meta:
        db_table = "votes"