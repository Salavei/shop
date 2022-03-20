# Generated by Django 4.0.3 on 2022-03-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_uuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveIntegerField(choices=[('In processing', 1), ('sent', 2)], db_index=True, default='1'),
        ),
    ]