from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.defaulttags import register
from io import BytesIO
from PIL import Image
from django.core.files import File

class eventspage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'college_events.html', context=None)

@register.filter
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