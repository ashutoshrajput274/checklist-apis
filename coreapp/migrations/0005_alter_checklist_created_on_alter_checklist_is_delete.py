# Generated by Django 4.2 on 2023-05-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0004_alter_checklist_is_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
