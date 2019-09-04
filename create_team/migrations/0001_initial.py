# Generated by Django 2.1.2 on 2019-09-03 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_registration', '0007_auto_20190903_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Leagues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(default='', max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team', models.CharField(max_length=250)),
                ('away_team', models.CharField(max_length=250)),
                ('match_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PlayerPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_eleven', models.IntegerField()),
                ('runs', models.FloatField()),
                ('fours', models.FloatField()),
                ('sixes', models.IntegerField()),
                ('strike_rate', models.IntegerField()),
                ('fifty', models.IntegerField()),
                ('hundred', models.IntegerField()),
                ('duck', models.IntegerField()),
                ('wickets', models.IntegerField()),
                ('maiden', models.IntegerField()),
                ('economy', models.IntegerField()),
                ('bonus', models.IntegerField()),
                ('catch', models.IntegerField()),
                ('runout_stumping', models.IntegerField()),
                ('total_points', models.FloatField()),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_team.Matches')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Players')),
            ],
        ),
        migrations.CreateModel(
            name='PrivateContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_code', models.CharField(max_length=10, unique=True)),
                ('participants', models.TextField()),
                ('contest_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Users')),
            ],
        ),
        migrations.CreateModel(
            name='SeriesList',
            fields=[
                ('Series_name', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('No_of_matches', models.IntegerField()),
                ('Home_team', models.CharField(max_length=250)),
                ('Away_team', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SeriesSquads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Series_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_team.SeriesList')),
                ('Squad_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Players')),
            ],
        ),
        migrations.CreateModel(
            name='TeamCreated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Users')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_team.Matches')),
            ],
        ),
        migrations.CreateModel(
            name='TeamPlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Players', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Players')),
                ('Team_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_team.TeamCreated')),
            ],
        ),
        migrations.CreateModel(
            name='UserTeamPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.FloatField()),
                ('team', models.TextField()),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_team.Matches')),
                ('series_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_team.SeriesList')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Users')),
            ],
        ),
        migrations.AddField(
            model_name='playerpoints',
            name='series_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_team.SeriesList'),
        ),
        migrations.AddField(
            model_name='leaguemembers',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_team.Leagues'),
        ),
        migrations.AddField(
            model_name='leaguemembers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Users'),
        ),
    ]
