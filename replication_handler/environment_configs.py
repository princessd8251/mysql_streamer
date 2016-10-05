# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import os


def is_avoid_internal_packages_set():
    return os.environ.get('FORCE_AVOID_INTERNAL_PACKAGES') and \
           os.environ.get('FORCE_AVOID_INTERNAL_PACKAGES').lower() == 'true'