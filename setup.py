from setuptools import setup, find_packages
#from distutils.core import setup

setup(
		name='Distutils',
		version='1.0',
		description='Python Distribution Utilities',
		author='Greg Ward',
		author_email='gward@python.net',
		url='https://www.python.org/sigs/distutils-sig/',
		packages=['distutils', 'distutils.command'],
     )
	 

import os #import path
import sys  

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellosite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)