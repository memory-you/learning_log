# Generated by Django 2.2.7 on 2019-11-22 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_ower'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='ower',
            new_name='owner',
        ),
    ]
