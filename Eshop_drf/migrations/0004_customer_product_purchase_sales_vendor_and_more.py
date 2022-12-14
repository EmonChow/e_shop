# Generated by Django 4.1.3 on 2022-11-15 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_drf', '0003_watchlist_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('mobile_number', models.IntegerField(max_length=15)),
                ('email_address', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField(max_length=15)),
                ('quantity', models.IntegerField(max_length=20)),
                ('exp_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=20)),
                ('date', models.DateField()),
                ('total_price', models.FloatField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop_drf.product')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=20)),
                ('date', models.DateField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop_drf.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop_drf.product')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('mobile_number', models.IntegerField(max_length=15)),
                ('email_address', models.EmailField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='platform',
        ),
        migrations.DeleteModel(
            name='StreamPlatform',
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
        migrations.AddField(
            model_name='purchase',
            name='vendor_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Eshop_drf.vendor'),
        ),
    ]
