from django.db import models

class election_data(models.Model):
      consti_name=models.CharField(max_length=200)
      last_winner=models.CharField(max_length=100)
      pre_winner=models.CharField(max_length=100)
      major_caste=models.CharField(max_length=50)
      
class candidate_data(models.Model):
      electiondata=models.ForeignKey(election_data)
      party=models.CharField(max_length=50)
      cast_support=models.CharField(max_length=50)
      campaigns=models.CharField(max_length=10)
      
def __unicode__(self):
      return str(self.name)
