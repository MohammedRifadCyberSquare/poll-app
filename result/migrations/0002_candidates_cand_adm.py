# Generated by Django 5.2 on 2025-04-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='cand_adm',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
