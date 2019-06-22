from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(filename)
    id=instance.email.split("@")[0]
    print(id)
    return 'student_profile/static/database/{}'.format(id+"."+filename.split(".")[-1])

def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im=im.resize((225,225))
    im.save(im_io, 'PNG', quality=75) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image

class Document(models.Model):

    name=models.CharField(max_length=255,blank=False)
    email=models.CharField(max_length=255,blank=False)
    insta_handle=models.CharField(max_length=255,blank=False)
    bio = models.CharField(max_length=255, blank=True)
    upload = models.ImageField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.upload)
        # set self.image to new_image
        self.upload = new_image
        # save
        super().save(*args, **kwargs)

class Email(models.Model):
    email=models.EmailField()