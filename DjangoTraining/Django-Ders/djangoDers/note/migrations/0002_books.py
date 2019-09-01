# Generated by Django 2.2.4 on 2019-09-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=300)),
                ('author', models.CharField(blank=True, max_length=70)),
                ('stock_info', models.PositiveIntegerField()),
                ('add_date', models.DateField()),
            ],
        ),
    ]
