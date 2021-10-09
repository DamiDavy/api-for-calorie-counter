# Generated by Django 3.2.7 on 2021-10-09 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foods', '0010_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailycalorieintake',
            name='username',
        ),
        migrations.AddField(
            model_name='dailycalorieintake',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]