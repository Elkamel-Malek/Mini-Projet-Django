# Generated by Django 3.0.5 on 2023-05-07 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0009_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Project Confirmed', 'Project Confirmed'), ('In progress', 'In progress'), ('Completed', 'Completed')], max_length=50, null=True),
        ),
    ]
