# Generated by Django 2.0 on 2020-11-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
