"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learn_english_server.settings")
    try:
        from django.core.management import execute_from_command_line

        print("\033[92mDjango is installed and ready to use.\033[0m")

    except ImportError as exc:
        # If Django is not installed, raise an ImportError with a helpful message
        msgError = (
            "Django is not installed. Please install it using 'pip install django'."
            if "django" in str(exc).lower()
            else "An unexpected error occurred while importing Django."
        )
        print(f"\033[33m{msgError}\033[0m")
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    print("\033[36mStarting server...\033[0m")
    main()
