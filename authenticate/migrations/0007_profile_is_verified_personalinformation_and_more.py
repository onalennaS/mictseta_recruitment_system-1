# Generated by Django 4.2.11 on 2024-06-05 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authenticate', '0006_profile_age_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_profile', models.CharField(max_length=225)),
                ('personal_website', models.CharField(max_length=225)),
                ('job_title', models.CharField(max_length=225)),
                ('current_employer', models.CharField(max_length=225)),
                ('years_of_expreince', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=225)),
                ('carear_level', models.CharField(max_length=225)),
                ('desired_job', models.CharField(max_length=225)),
                ('job_location', models.CharField(max_length=225, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddressInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address_line', models.CharField(max_length=225, null=True)),
                ('city', models.CharField(max_length=225)),
                ('province', models.CharField(max_length=225)),
                ('postal_code', models.CharField(max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
