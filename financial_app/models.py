from django.db import models

# Create your models here.

class UserFinancialdata(models.Model):
    user_id = models.CharField(max_length=200, blank=True, null=True)
    clerk_file = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return str(self.user_id) if self.user_id else "userid is none"
