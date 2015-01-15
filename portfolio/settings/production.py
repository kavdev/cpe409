from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# ======================================================================================================== #
#                                      Session/Security Configuration                                      #
# ======================================================================================================== #

# Cookie Settings
SESSION_COOKIE_NAME = 'cpe409SessionID'
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

ALLOWED_HOSTS = [
    'cpe409.kavanaughdevelopment.com',
    'cpe409.kavdev.io'
]
