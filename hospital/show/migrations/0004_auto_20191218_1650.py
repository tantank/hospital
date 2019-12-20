# Generated by Django 3.0 on 2019-12-18 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_auto_20191218_1606'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hospital',
            new_name='Hospital강원',
        ),
        migrations.CreateModel(
            name='Hospital충북',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital충남',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital전북',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital전남',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital인천',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital울산',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital세종시',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital서울',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital부산',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital대전',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital대구',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital광주',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital경북',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital경남',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital경기',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sggucdnm', models.CharField(max_length=8)),
                ('yadmnm', models.CharField(max_length=15)),
                ('clcdnm', models.CharField(max_length=6)),
                ('npaykornm', models.CharField(max_length=25)),
                ('maxprc', models.IntegerField()),
                ('minprc', models.IntegerField()),
                ('url', models.URLField()),
                ('sidocdnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.City')),
            ],
        ),
    ]
