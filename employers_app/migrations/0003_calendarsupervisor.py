# Generated by Django 4.0.3 on 2022-03-29 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employers_app', '0002_alter_employee_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarSupervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date', models.DateField(verbose_name='Data spotkania')),
                ('note', models.TextField(verbose_name='Notatka')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='employers_app.employee', verbose_name='Podopieczny')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='calendar_supervisor', to='employers_app.employee', verbose_name='Właściciel')),
            ],
        ),
    ]