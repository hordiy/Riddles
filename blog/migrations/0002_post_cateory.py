# Generated by Django 2.1.3 on 2019-01-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cateory',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Category'),
        ),
    ]