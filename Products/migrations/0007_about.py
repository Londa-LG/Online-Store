# Generated by Django 3.0.6 on 2020-06-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('faq', models.TextField()),
            ],
        ),
    ]
