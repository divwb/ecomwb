# Generated by Django 4.1.3 on 2023-02-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_alter_product_category_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('ML', 'Milk'), ('PN', 'Paneer'), ('Ic', 'Icecream'), ('GH', 'Ghee'), ('CZ', 'Cheese')], max_length=2),
        ),
    ]
