# Generated by Django 4.1.7 on 2023-03-06 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_course_students_remove_course_teacher_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='senroller_user',
            new_name='enroller_user',
        ),
    ]
