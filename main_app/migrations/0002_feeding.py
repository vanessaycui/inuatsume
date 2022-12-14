# Generated by Django 4.1.4 on 2022-12-13 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('food', models.CharField(choices=[('B', 'Breakfast'), ('D', 'Dinner'), ('S', 'Snacks')], default='B', max_length=1)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.dog')),
            ],
        ),
    ]
