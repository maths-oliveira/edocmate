# Generated by Django 4.1.7 on 2023-03-18 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_dossier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dossier',
            name='document',
        ),
        migrations.AddField(
            model_name='dossier',
            name='documents',
            field=models.ManyToManyField(related_name='dossiers', to='documents.document'),
        ),
    ]
