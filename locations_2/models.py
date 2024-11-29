from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils import timezone
from django.conf import settings
from cloudinary.models import CloudinaryField



class User(AbstractUser):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender=models.CharField(max_length=30,choices=GENDER, null=True)
    age=models.IntegerField(null=True)
    phone_number = models.CharField(max_length=13, null=True)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image = models.ImageField(default='default.jpd', upload_to='profile/')

	def __str__(self):
		return self.user.username

class Location(models.Model):
	poster=models.ForeignKey(User, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=40, null=True)
	country = models.CharField(max_length=60)
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	city = models.CharField(max_length=30, null=True, blank=True)
	district = models.CharField(max_length=50, null=True, blank=True)
	sector = models.CharField(max_length=50, null=True, blank=True)
	status = models.BooleanField(default=False)
	reported_time = models.DateTimeField(default=timezone.now)
	image = CloudinaryField('image', folder='properties')
	description = models.TextField(default='devastation')

	def __str__(self):
		return self.title


class Contact(models.Model):
	name=models.CharField(max_length=100,null=True,blank=True)
	email=models.EmailField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.TextField(max_length=3000)
	created_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


	