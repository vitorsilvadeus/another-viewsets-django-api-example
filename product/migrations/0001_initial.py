# Generated by Django 3.1.1 on 2020-09-07 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=8)),
                ('price', models.DecimalField(decimal_places=3, max_digits=12)),
                ('cost', models.DecimalField(decimal_places=3, max_digits=12)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KitRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('discount', models.DecimalField(decimal_places=3, max_digits=6)),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.kit')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='kit',
            name='products',
            field=models.ManyToManyField(through='product.KitRelation', to='product.Product'),
        ),
    ]
