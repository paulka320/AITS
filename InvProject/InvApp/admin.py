from django.contrib import admin
from .models import CustomUser,Internship_placement,WeeklyLog,EvaluationCriteria,Evaluation
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Internship_placement)
admin.site.register(WeeklyLog)
admin.site.register(EvaluationCriteria)
admin.site.register(Evaluation)
