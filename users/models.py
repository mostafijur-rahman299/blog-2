import string, os, random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from sorl.thumbnail import ImageField

from PIL import Image

def get_filepath(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext  

def upload_filename_ext(instnace, filename):
    newFilename = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 7)
    newFilename = "".join(newFilename)
    name, ext = get_filepath(filename)
    return f'{newFilename}{ext}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_filename_ext, default="a.jpg")

    def __str__(self):
        return str(self.user)

    # image resize
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)




# profile create signals
def user_profile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        new_profile = UserProfile.objects.create(user=instance)

post_save.connect(user_profile_receiver, sender=User)


def profile_save_receiver(sender, instance, *args, **kwargs):
    instance.userprofile.save()

post_save.connect(profile_save_receiver, sender=User)
