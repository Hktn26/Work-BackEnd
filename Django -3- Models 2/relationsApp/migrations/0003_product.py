# Generated by Django 4.2.6 on 2023-10-31 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationsApp', '0002_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=64)),
                ('product', models.CharField(max_length=50)),
                ('account', models.ManyToManyField(to='relationsApp.account')),
            ],
        ),
    ]
