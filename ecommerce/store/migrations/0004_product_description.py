# Generated by Django 4.2.3 on 2023-07-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.CharField(max_length=500, null=True),
        ),
    ]