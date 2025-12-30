from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()

        # Create users (super heroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com'},
            {'username': 'superman', 'email': 'superman@dc.com'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com'},
        ]
        marvel_users = [User.objects.create(**hero) for hero in marvel_heroes]
        dc_users = [User.objects.create(**hero) for hero in dc_heroes]

        # Create teams
        marvel_team = Team.objects.create(name='Marvel')
        marvel_team.members.set(marvel_users)
        dc_team = Team.objects.create(name='DC')
        dc_team.members.set(dc_users)

        # Create workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes', suggested_for='All')
        workout2 = Workout.objects.create(name='Flight Training', description='Aerobic workout for flyers', suggested_for='Superman, Ironman, Wonder Woman')

        # Create activities
        Activity.objects.create(user=marvel_users[0], activity_type='Tech Training', duration=60, calories_burned=500, date='2025-12-30')
        Activity.objects.create(user=dc_users[0], activity_type='Martial Arts', duration=45, calories_burned=400, date='2025-12-30')

        # Create leaderboard
        Leaderboard.objects.create(user=marvel_users[0], score=100, rank=1)
        Leaderboard.objects.create(user=dc_users[0], score=90, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
