# Generated by Django 4.2.19 on 2025-03-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_orden_fecha_alter_orden_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='numero_orden',
            field=models.CharField(max_length=10),
        ),
    ]
