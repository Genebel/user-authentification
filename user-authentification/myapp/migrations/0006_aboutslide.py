# Generated by Django 4.1.6 on 2023-02-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_about_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=200)),
            ],
        ),
    ]