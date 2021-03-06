# Generated by Django 3.0.6 on 2020-05-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.TextField()),
                ('pax', models.IntegerField()),
                ('venue', models.CharField(max_length=255)),
                ('price', models.TextField(max_length=50)),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
