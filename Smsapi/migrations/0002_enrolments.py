# Generated by Django 4.2.5 on 2023-11-27 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Smsapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrolments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Smsapi.courses')),
                ('student_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Smsapi.students')),
            ],
        ),
    ]
