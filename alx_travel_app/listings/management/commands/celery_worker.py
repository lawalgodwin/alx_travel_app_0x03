import shlex
import sys
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery():
    """A function that restarts the celery worker"""
    celery_worker_cmd = "celery -A alx_travel_app worker"
    cmd = "taskkill /f /t /im celery.exe"  if sys.platform == "win32" else f'pkill -f "{celery_worker_cmd}"'
    # kill celery process
    subprocess.call(shlex.split(cmd))
    # run celery process
    subprocess.call(shlex.split(f"{celery_worker_cmd} --loglevel=info"))

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Starting celery worker with autoreload...')
        autoreload.run_with_reloader(restart_celery)