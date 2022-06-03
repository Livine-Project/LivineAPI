# Generated by Django 3.2.6 on 2022-05-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_recipemodel_time_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipemodel',
            name='calories',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='directions',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='directions_in_arabic',
            field=models.TextField(default=''),
        ),
    ]
