# Generated by Django 3.0.4 on 2020-03-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='man',
            name='Location_dead',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]