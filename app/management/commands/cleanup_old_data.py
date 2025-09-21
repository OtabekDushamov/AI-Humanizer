from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from app.models import User, Request


class Command(BaseCommand):
    help = 'Clean up old users and requests'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=30,
            help='Number of days to keep data (default: 30)',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without actually deleting',
        )

    def handle(self, *args, **options):
        days = options['days']
        dry_run = options['dry_run']
        
        cutoff_date = timezone.now() - timedelta(days=days)
        
        # Find old users (users with no recent activity)
        old_users = User.objects.filter(last_active__lt=cutoff_date)
        old_requests = Request.objects.filter(created_at__lt=cutoff_date)
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING(
                    f'DRY RUN: Would delete {old_users.count()} users and {old_requests.count()} requests older than {days} days'
                )
            )
            
            # Show some examples
            if old_users.exists():
                self.stdout.write('\nExample old users:')
                for user in old_users[:5]:
                    self.stdout.write(f'  - {user}')
            
            if old_requests.exists():
                self.stdout.write('\nExample old requests:')
                for req in old_requests[:5]:
                    self.stdout.write(f'  - {req}')
        else:
            # Actually delete the data
            deleted_requests = old_requests.count()
            deleted_users = old_users.count()
            
            old_requests.delete()
            old_users.delete()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully deleted {deleted_users} users and {deleted_requests} requests older than {days} days'
                )
            )
