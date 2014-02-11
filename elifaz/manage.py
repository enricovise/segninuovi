#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elifaz.settings")
    
    # Added for Django-configuration
    os.environ.setdefault('DJANGO_CONFIGURATION', 'DevelopmentSettings')

    # Changed for Django-configuration
    # from django.core.management import execute_from_command_line
    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
