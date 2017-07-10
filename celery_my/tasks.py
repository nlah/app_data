
"""
"A universal convention supplies all of maintainability,
clarity, consistency, and a foundation for good programming habits too.
What it doesn't do is insist that you follow it against your will. That's Python!"
—Tim Peters on comp.lang.python, 2001-06-16
"""
from pymongo import MongoClient
from plots.upc import UpcWalmart
from . celery import app
from plots.models import WalmartModel
from django.utils import timezone


@app.task
def add():
    """
    Update the database on upc
    """
    walmart = UpcWalmart(app.conf['CELERY_WALMART_KEY'])
    walmart.update(WalmartModel.objects, timezone)
