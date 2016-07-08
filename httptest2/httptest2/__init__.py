# -*- coding: utf-8 -*-
__version__ = '0.1.0'
__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace('-', '.', 1).split('.')])

#from __future__ import absolute_import
from httptest2.taskapp import celery
#import httptest2.testmodule.celery_task
#from testmodule import views
