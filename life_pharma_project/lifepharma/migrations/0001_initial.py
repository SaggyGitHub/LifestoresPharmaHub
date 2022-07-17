# Generated by Django 2.2.6 on 2022-07-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=265)),
                ('description', models.TextField()),
                ('sku', models.CharField(max_length=265)),
                ('price', models.BigIntegerField()),
                ('image', models.URLField()),
            ],
        ),
    ]
