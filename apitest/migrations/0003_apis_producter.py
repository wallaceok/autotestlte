# Generated by Django 2.1.4 on 2019-05-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_apis'),
    ]

    operations = [
        migrations.AddField(
            model_name='apis',
            name='producter',
            field=models.CharField(max_length=200, null=True, verbose_name='产品负责人'),
        ),
    ]