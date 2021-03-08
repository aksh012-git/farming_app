from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from management.models import crop


# user record model

class userProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    mobileNo = models.CharField(max_length=10, blank=True, null=True)
    ProfilePic = models.ImageField(
        upload_to='user/profilePics/', default="user/profilePics/defaultpic.jpg", null=True, blank=True)

    def __str__(self):
        return self.user.username


class UserRecord(models.Model):
 
 #choice for thw soil
    sandySoil = "Sandy soil"
    siltSoil = "Silt Soil"
    claySoil = "Clay Soil"
    loamySoil = "Loamy Soil"
    SOIL_CHOICES = (
        (sandySoil, "Sandy Soil"),
        (siltSoil, "Silt Soil"),
        (claySoil, "Clay Soil"),
        (loamySoil, "Loamy Soil"),
    )

    #choice for approve record

    approved="approved"
    pending="pending"
    rejected="rejected"

    Approvement=((approved,"approved"),
    (pending,"pending"),
    (rejected,"rejected"),)

    recordId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False, null=False)
    mobileNo = models.CharField(max_length=10, blank=False, null=False)
    farmaddress = models.CharField(max_length=150, blank=False, null=False)
    farmArea = models.IntegerField(default=0)
    soilType = models.CharField(max_length=11, choices=SOIL_CHOICES, default=siltSoil)
    moneyDemand = models.IntegerField(default=0)
    farmImage = models.ImageField(upload_to='user/farm/', default="")
    extraComment = models.TextField()
    status=models.CharField(max_length=11, choices=Approvement, default=pending)
    crop = models.ManyToManyField(crop,blank=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

# contact us model


class ContactUs(models.Model):
    msg_id = models.AutoField(primary_key="true")
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=10, default='')
    desc = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name
