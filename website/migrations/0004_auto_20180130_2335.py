# Generated by Django 2.0 on 2018-01-30 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
