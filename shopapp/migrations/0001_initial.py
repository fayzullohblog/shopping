# Generated by Django 4.0.1 on 2022-07-22 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountapp', '0001_initial'),
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='BrandModel_Image')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WidListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accountapp.usermodel')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homeapp.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='InformationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=150)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homeapp.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ImageModel_Image')),
                ('title', models.CharField(max_length=50)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homeapp.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accountapp.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accountapp.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='CartItimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('total', models.IntegerField()),
                ('order_time', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopapp.cartmodel')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homeapp.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='BannerListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagebackground', models.ImageField(upload_to='BannerModel_Image')),
                ('imageproduct', models.ImageField(upload_to='ProductModel_Image')),
                ('title', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.categorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='AdvertisModel_Image')),
                ('title', models.CharField(max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.productmodel')),
            ],
        ),
    ]