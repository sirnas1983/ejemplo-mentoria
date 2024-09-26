# Generated by Django 5.1.1 on 2024-09-26 13:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_vencimiento', models.DateTimeField()),
                ('tarea', models.TextField()),
                ('is_concluida', models.BooleanField(default=False)),
            ],
        ),
    ]
