# Generated by Django 2.0.6 on 2018-06-13 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DivingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name="Date et heure d'arrivée")),
                ('extra_infos', models.TextField(verbose_name='Infos supp')),
            ],
        ),
        migrations.CreateModel(
            name='PersonInChargeOf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Personne en charge')),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Site de plongée')),
            ],
        ),
        migrations.AddField(
            model_name='divingevents',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.PersonInChargeOf'),
        ),
        migrations.AddField(
            model_name='divingevents',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Places'),
        ),
    ]