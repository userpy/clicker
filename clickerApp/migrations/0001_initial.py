# Generated by Django 2.2.6 on 2019-10-30 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=250)),
            ],
        ),
    ]
