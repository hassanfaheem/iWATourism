# Generated by Django 4.2.7 on 2023-11-14 09:28

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=25)),
                ('alternative_contact_number', models.CharField(max_length=25)),
                ('passport_number', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='GroupTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('from_city', models.CharField(choices=[('Bengaluru', 'Bengaluru'), ('Chennai', 'Chennai'), ('Mumbai', 'Mumbai'), ('Hyderabad', 'Hyderabad'), ('Lucknow', 'Lucknow'), ('Delhi', 'Delhi'), ('Jaipur', 'Jaipur'), ('Ahmedabad', 'Ahmedabad'), ('Kolkata', 'Kolkata'), ('Thiruvananthapuram', 'Thiruvananthapuram')], default='', max_length=50)),
                ('to_city', models.CharField(choices=[('Abu Dhabi', 'Abu Dhabi'), ('Dubai', 'Dubai'), ('Sharjah', 'Sharjah')], default='', max_length=50)),
                ('days', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('nights', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('description', ckeditor.fields.RichTextField()),
                ('included', models.TextField()),
                ('not_included', models.TextField()),
                ('total_seats', models.IntegerField()),
                ('remaining_seats', models.IntegerField()),
                ('booking_end_date', models.DateTimeField()),
                ('sold_out', models.BooleanField(default=False)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('people', models.IntegerField()),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Web.grouptour')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.SmallIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('description', ckeditor.fields.RichTextField()),
                ('group_tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.grouptour')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consent', models.BooleanField()),
                ('booking_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=13)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=13)),
                ('paid', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Processing', 'Processing'), ('Booked', 'Booked')], default='processing', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('add_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Web.addon')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.customer')),
                ('group_tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Web.grouptour')),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Web.package')),
            ],
        ),
        migrations.AddField(
            model_name='addon',
            name='group_tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Web.grouptour'),
        ),
    ]