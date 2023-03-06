# Generated by Django 4.1.7 on 2023-03-06 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_userprogress_course_alter_userprogress_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='videos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='vidoes_time',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='duration',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='videos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.course'),
        ),
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]