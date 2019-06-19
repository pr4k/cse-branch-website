from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(filename)
    id=instance.email.split("@")[0]
    print(id)
    return 'student_profile/static/database/{}'.format(id+"."+filename.split(".")[-1])

class Document(models.Model):

    name=models.CharField(max_length=255,blank=False)
    email=models.CharField(max_length=255,blank=False)
    insta_handle=models.CharField(max_length=255,blank=False)
    bio = models.CharField(max_length=255, blank=True)
    upload = models.ImageField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Email(models.Model):
    email=models.EmailField()