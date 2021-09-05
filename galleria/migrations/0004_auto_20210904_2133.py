# Generated by Django 3.2.6 on 2021-09-04 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0003_auto_20210904_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='galleria.categories'),
        ),
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='galleria.location'),
        ),
    ]
