# Generated by Django 4.1.7 on 2023-04-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_alter_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]