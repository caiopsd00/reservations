# Generated by Django 4.2.7 on 2023-11-08 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
                ('administrador', models.BooleanField()),
            ],
        ),
    ]
