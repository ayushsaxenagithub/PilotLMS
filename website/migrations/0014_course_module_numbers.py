# Generated by Django 4.1.7 on 2023-03-09 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_remove_course_modules'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='module_numbers',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
