# Generated by Django 2.0.8 on 2018-09-15 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofile',
            name='class_TG',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.classes'),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='last_student_rollno',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='start_student_rollno',
            field=models.CharField(max_length=6, null=True),
        ),
    ]