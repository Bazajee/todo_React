# Generated by Django 4.2.10 on 2024-02-29 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=50)),
                ('hash', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField()),
                ('body', models.CharField(max_length=50)),
                ('taskList_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_api.tasklist')),
            ],
        ),
    ]
