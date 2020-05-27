from django.db import models

# Create your models here.
class Candidate(models.Model):
    CandidateID = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Contact = models.CharField(max_length=20)

class Trainer(models.Model):
    CandidateID = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Contact = models.CharField(max_length=20)