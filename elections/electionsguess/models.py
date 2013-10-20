from django.db import models

class election_data(models.Model):
      consti_name=models.CharField(max_length=200)
      last_winner=models.CharField(max_length=100)
      pre_winner=models.CharField(max_length=100)
      major_caste=models.CharField(max_length=50)
