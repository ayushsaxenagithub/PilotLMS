# Generated by Django 4.1.7 on 2023-03-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_organization_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='founded_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
