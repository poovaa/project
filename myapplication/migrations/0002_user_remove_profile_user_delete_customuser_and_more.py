# Generated by Django 5.1.2 on 2024-10-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('password', models.TextField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
