# Generated by Django 4.2.7 on 2023-11-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0004_rename_paid_booking_total_amount_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(choices=[('Debit/Credit Card', 'Debit/Credit Card')], default='Debit/Credit Card', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Booked', 'Booked')], default='Processing', max_length=50),
        ),
    ]