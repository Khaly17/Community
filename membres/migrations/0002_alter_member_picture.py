# Generated by Django 3.2.5 on 2021-08-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
