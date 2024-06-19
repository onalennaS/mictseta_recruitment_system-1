# Generated by Django 4.2.11 on 2024-06-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Education',
            new_name='Academic',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='application_deadline',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='id_copy',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='other_documents',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='proof_of_residence',
        ),
        migrations.AddField(
            model_name='requirement',
            name='description',
            field=models.CharField(default=' ', max_length=10),
            preserve_default=False,
        ),
    ]
