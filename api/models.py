from django.db import models
from .validators import validate_file_type, validate_size, validate_file_length
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/', validators=[validate_file_type, validate_size, validate_file_length])
    uploaded_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}' 
