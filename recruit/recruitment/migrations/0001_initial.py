# Generated by Django 2.0.6 on 2018-06-09 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_name', models.CharField(max_length=200)),
                ('marks_percentage', models.FloatField()),
                ('institution_name', models.TextField()),
                ('year_of_passed_out', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('project_description', models.TextField()),
                ('duration_from', models.DateField()),
                ('duration_to', models.DateField()),
                ('role_and_responsibility', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SkillsDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200)),
                ('years_of_experience', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=30)),
                ('address', models.TextField(blank=True, null=True)),
                ('total_experience', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='experiencedetails',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.UserProfile'),
        ),
        migrations.AddField(
            model_name='educationaldetails',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.UserProfile'),
        ),
    ]
