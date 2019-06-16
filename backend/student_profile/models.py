from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format("prakhar" ,"filename")

class Document(models.Model):
    insta_handle=models.CharField(max_length=255,blank=False)
    bio = models.CharField(max_length=255, blank=True)
    upload = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)