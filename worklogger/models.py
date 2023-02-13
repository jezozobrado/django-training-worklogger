from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=255)

    logger = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        # return self.name
        # return f"{self.logger.username} worked on project {self.project_name}"
        return self.project_name

# class Assignment(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

#     developer = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f"{self.developer.username} worked on project {self.project}"


class Log(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

    date = models.DateField()

    hours = models.FloatField()

    remarks = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.project.logger.username} logged {self.hours} hours on {self.project.project_name}"
