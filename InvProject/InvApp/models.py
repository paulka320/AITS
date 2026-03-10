from django.db import models

# Create your models here.
class CustomUser(models.Model):
    person_id = models.AutoField(primary_key=True)
    student_name =models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Name:{self.student_name}"
        return f"Role:{self.role}"
        
        
        
class Internship_placement(models.Model):
    person_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
    
    def __str__(self):
        return f"Student Name:{self.student_name}"
        return f"Organization:{self.organization}"
        return f"Supervisor:{self.supervisor}"
        
class WeeklyLog(models.Model):
    person_id = models.AutoField(primary_key=True)
    internship_placement = models.CharField(max_length=100)
    week_number = models.IntegerField()
    activites = models.TextField()
    log_date = models.DateField()
    
    def __str__(self):
        return f"Internship Placement:{self.internship_placement}"
        return f"Week Number:{self.week_number}"
        return f"Activities:{self.activities}"
        return f"Log Date:{self.log_date}"
        
class EvaluationCriteria(models.Model):
    person_id = models.AutoField(primary_key=True)
    criteria_name = models.CharField(max_length=100)
    description = models.TextField()
    max_score = models.IntegerField()
    
    def __str__(self):
        return f"Criteria:{self.criteria_name}"
        return f"Description:{self.description}"
        return f"Score:{self.max_score}"
        
        
class Evaluation(models.Model):
    person_id = models.AutoField(primary_key=True)
    #weekly_logs = models.
    score = models.IntegerField()
    comments = models.TextField()
    
    def __str__(self):
        return f"Score:{self.score}"
        return f"Comments:{self.comments}"