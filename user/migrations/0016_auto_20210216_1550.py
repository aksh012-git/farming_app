# Generated by Django 3.1.6 on 2021-02-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20210216_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edituserprofile',
            name='Change_photo',
            field=models.ImageField(default='user/Profile_pic/default-user.png', upload_to='user/profile_pic/'),
        ),
    ]
