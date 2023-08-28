# Generated by Django 4.2.3 on 2023-08-27 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lms_app.category'),
        ),
    ]
