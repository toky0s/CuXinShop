# Generated by Django 3.1 on 2020-08-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_auto_20200811_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag_full_name',
            field=models.CharField(default='Fullname is none', max_length=100),
        ),
    ]