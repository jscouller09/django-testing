# Generated by Django 4.0.5 on 2022-06-14 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0004_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(),
        ),
    ]
