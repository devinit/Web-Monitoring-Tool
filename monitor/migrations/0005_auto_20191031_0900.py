# Generated by Django 2.2.6 on 2019-10-31 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_auto_20191030_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statusupdate',
            name='status',
        ),
        migrations.RemoveField(
            model_name='statusupdate',
            name='task',
        ),
        migrations.RemoveField(
            model_name='task',
            name='server',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.RemoveField(
            model_name='watcher',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='watcher',
            name='switch_status',
        ),
        migrations.RemoveField(
            model_name='watcher',
            name='task',
        ),
        migrations.RemoveField(
            model_name='watcher',
            name='watch_status',
        ),
        migrations.AddField(
            model_name='watcher',
            name='expected_value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watcher',
            name='method',
            field=models.CharField(blank=True, choices=[('timestamp_uptodate', 'Server responding'), ('free_memory_percent', 'Free memory percent'), ('pid', 'Process ID'), ('docker_id', 'Docker ID'), ('generic', 'Generic')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='watcher',
            name='operator',
            field=models.CharField(blank=True, choices=[('lt', 'Less than'), ('le', 'Less Than or Equal To'), ('eq', 'Equal To'), ('ne', 'Not Equal'), ('ge', 'Greater Than or Equal'), ('gt', 'Greater Than'), ('len', 'Length'), ('in', 'String In')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='watcher',
            name='servers',
            field=models.ManyToManyField(to='monitor.Server'),
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='StatusUpdate',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
