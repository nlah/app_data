import os
from django.core.management.base import BaseCommand, CommandError

from celery_my.start import celery_start


class Command(BaseCommand):

    def handle(self, *args, **options):
        celery_start()
