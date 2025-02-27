# Generated by Django 4.2.19 on 2025-02-27 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_orden', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Viga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_viga', models.CharField(max_length=100)),
                ('cantidad', models.PositiveIntegerField()),
                ('medidas', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vigas', to='api.orden')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='produccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordenes', to='api.produccion'),
        ),
    ]
