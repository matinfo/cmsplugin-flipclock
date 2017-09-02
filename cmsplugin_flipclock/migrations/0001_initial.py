# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlipClockPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', parent_link=True, serialize=False, related_name='cmsplugin_flipclock_flipclockplugin', primary_key=True, auto_created=True)),
                ('clock_face', models.CharField(default='HourlyCounter', choices=[('HourlyCounter', 'Hourly Counter'), ('MinuteCounter', 'Minute Counter'), ('DailyCounter', 'Daily Counter'), ('TwelveHourClock', '12hr Clock'), ('TwentyFourHourClock', '24hr Clock'), ('Counter', 'General Counter')], max_length=20, help_text='This is the name of the clock that is used to build the clock display. The default value is HourlyCounter', verbose_name='clockFace')),
                ('auto_play', models.BooleanField(default=True, help_text='If this is set to false, the clock will not automatically add the play class to start the animation. If the play class is not added, the clock value can still change but with no animation. The default value is <i>true</i>.', verbose_name='autoPlay')),
                ('auto_start', models.BooleanField(default=True, help_text='If this is set to false, the clock will not auto start. The default value is <i>true</i>.', verbose_name='autoStart')),
                ('countdown', models.BooleanField(default=False, help_text='If this is set to true, the clock will count down instead of up. The default value is <i>false</i>.', verbose_name='Countdown')),
                ('show_seconds', models.BooleanField(default=True, help_text='If this is set to true, the clock will show <i>second</i>. Compatible with clockFace Hourly, Minute and Daily counter.', verbose_name='showSeconds')),
                ('date', models.DateTimeField(blank=True, null=True, help_text='Start or end date depending if <i>countdown</i> set. Compatible with clockFace Hourly, Minute and Daily counter.', verbose_name='date & time')),
                ('numbers', models.IntegerField(default=0, help_text='Compatible with clockFace General counter.', verbose_name='Number')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
