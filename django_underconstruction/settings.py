from django.conf import settings


if not hasattr(settings, 'UNDER_CONSTRUCTION'):
    settings.UNDER_CONSTRUCTION = False

if not hasattr(settings, 'UNDER_CONSTRUCTION_TEMPLATE'):
    settings.UNDER_CONSTRUCTION_TEMPLATE = 'django_underconstruction/construction.html'
