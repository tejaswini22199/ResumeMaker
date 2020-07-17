# Generated by Django 3.0.7 on 2020-07-05 13:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=55)),
                ('position', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=40)),
                ('personal_profile', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='educ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=55)),
                ('school_location', models.CharField(max_length=55)),
                ('Degree', models.CharField(max_length=55)),
                ('CGPA', models.CharField(max_length=55)),
                ('Field_of_Study', models.CharField(max_length=55)),
                ('Expected_year_of_grad', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='extrafield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('explanation', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='workexp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=55)),
                ('employer', models.CharField(max_length=55)),
                ('city', models.CharField(max_length=55)),
                ('state', models.CharField(max_length=55)),
                ('startdate', models.DateField(max_length=55)),
                ('enddate', models.DateField(max_length=55)),
                ('jobdesc', models.CharField(max_length=2000)),
            ],
        ),
    ]