# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_flipclock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flipclockplugin',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(blank=True, verbose_name='time zone', default='Europe/London', null=True, help_text='If set force the timezone used, otherwise use user timezone.'),
        ),
        migrations.AlterField(
            model_name='flipclockplugin',
            name='auto_play',
            field=models.BooleanField(help_text='If selected, the clock will not automatically add the play class to start the animation.', verbose_name='autoPlay', default=True),
        ),
        migrations.AlterField(
            model_name='flipclockplugin',
            name='auto_start',
            field=models.BooleanField(help_text='If this is set to false, the clock will not auto start.', verbose_name='autoStart', default=True),
        ),
        migrations.AlterField(
            model_name='flipclockplugin',
            name='clock_face',
            field=models.CharField(max_length=20, help_text='This is the name of the clock that is used to build the clock display.', choices=[('HourlyCounter', 'Hourly Counter'), ('MinuteCounter', 'Minute Counter'), ('DailyCounter', 'Daily Counter'), ('TwelveHourClock', '12hr Clock'), ('TwentyFourHourClock', '24hr Clock'), ('Counter', 'General Counter')], verbose_name='clockFace', default='HourlyCounter'),
        ),
        migrations.AlterField(
            model_name='flipclockplugin',
            name='countdown',
            field=models.BooleanField(help_text='If seleted, the clock will count down instead of up.', verbose_name='Countdown', default=False),
        ),
        migrations.AlterField(
            model_name='flipclockplugin',
            name='numbers',
            field=models.IntegerField(help_text='Compatible with clockFace General counter.', verbose_name='number', default=0),
        ),
        migrations.AlterField(
            model_name='flipclockplugin',
            name='show_seconds',
            field=models.BooleanField(help_text='If selected, the clock will show <i>second</i>. Compatible with clockFace Hourly, Minute and Daily counter.', verbose_name='showSeconds', default=True),
        ),
    ]
