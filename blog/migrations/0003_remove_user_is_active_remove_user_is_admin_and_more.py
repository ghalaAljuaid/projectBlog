# Generated by Django 5.0 on 2023-12-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user_is_active_user_is_admin_user_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
