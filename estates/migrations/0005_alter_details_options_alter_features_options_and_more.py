# Generated by Django 4.0.4 on 2022-06-25 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estates', '0004_details_alter_features_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'verbose_name': 'Детали', 'verbose_name_plural': 'Детали'},
        ),
        migrations.AlterModelOptions(
            name='features',
            options={'verbose_name': 'Особенности', 'verbose_name_plural': 'Особенности'},
        ),
        migrations.AlterField(
            model_name='details',
            name='estate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='details', serialize=False, to='estates.estate', verbose_name='Имущество'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estates', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='estate_type',
            field=models.CharField(choices=[('H', 'Дом'), ('F', 'Квартира')], max_length=1, verbose_name='Вид собственности'),
        ),
        migrations.AlterField(
            model_name='features',
            name='details',
            field=models.ManyToManyField(related_name='features', to='estates.details', verbose_name='Детали'),
        ),
        migrations.AlterField(
            model_name='features',
            name='kind',
            field=models.CharField(choices=[('HF', 'Пол с подогревом'), ('PO', 'Двор'), ('GN', 'Сад'), ('SP', 'Бассейн')], max_length=3, verbose_name='Тип'),
        ),
    ]
