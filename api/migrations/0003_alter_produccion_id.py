# Generated by Django 4.2.19 on 2025-03-01 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_produccion_fecha_alter_produccion_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='id',
            field=models.CharField(editable=False, max_length=20, primary_key=True, serialize=False),
        ),
    ]
