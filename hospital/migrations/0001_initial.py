# Generated by Django 3.0.6 on 2022-10-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('subway', models.CharField(max_length=50)),
                ('location', models.TextField()),
                ('location2', models.TextField()),
                ('ratings', models.CharField(max_length=200)),
                ('reviews', models.IntegerField()),
                ('open_hour', models.TextField()),
                ('restAt', models.TextField()),
                ('labels', models.TextField()),
                ('animal_keyword', models.TextField()),
                ('service_keyword', models.TextField()),
                ('is_favorite', models.TextField()),
                ('now_open', models.BooleanField(default=True)),
                ('naver_map', models.URLField()),
                ('website', models.URLField()),
                ('instagram', models.URLField()),
                ('youtube', models.URLField()),
            ],
        ),
    ]