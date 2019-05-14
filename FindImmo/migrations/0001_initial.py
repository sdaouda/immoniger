# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-10 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomPrenom', models.CharField(blank=True, max_length=80, null=True)),
                ('Phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Localite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localite', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('dimmension', models.CharField(blank=True, max_length=20, null=True)),
                ('numeroParcelle', models.CharField(blank=True, default='n/a', max_length=15, null=True)),
                ('lotissement', models.CharField(blank=True, default='n/a', max_length=200, null=True)),
                ('actsession', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to='products/imgs/')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='products/imgs/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products/imgs/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products/imgs/')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('nbChambre', models.PositiveIntegerField()),
                ('nbDouche', models.PositiveIntegerField()),
                ('action_type', models.CharField(blank=True, choices=[('L', 'LOCATION'), ('V', 'VENTE')], default='L', help_text='Vente/Location', max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='FindImmo.Category')),
                ('localite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FindImmo.Localite')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='TypeImmo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('phone3', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=20, null=True)),
                ('ville', models.CharField(max_length=20)),
                ('quartier', models.CharField(blank=True, max_length=20, null=True)),
                ('localization', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(db_index=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='FindImmo.TypeImmo'),
        ),
        migrations.AddField(
            model_name='product',
            name='vendeur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FindImmo.Dealer'),
        ),
        migrations.AddField(
            model_name='product',
            name='zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FindImmo.Zone'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
