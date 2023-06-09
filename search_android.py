import subprocess
import random
import string

SEARCH_URL_BASE = "https://www.bing.com/search?q="
PACKAGE_NAME = 'com.microsoft.emmx'  # Package name of Microsoft Edge
ACTIVITY_NAME = 'com.microsoft.ruby.Main'


def generate_random_query(length=10):
    """
    Generates a random search query of specified length.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def perform_searches(num_searches):
    """
    Performs a specified number of searches with random queries using Microsoft Edge via adb command.
    """
    search_urls = [
        f"{SEARCH_URL_BASE}{generate_random_query()}" for _ in range(num_searches)]
    adb_command = ['adb', 'shell', 'am', 'start', '-n',
                   f'{PACKAGE_NAME}/{ACTIVITY_NAME}', '-a', 'android.intent.action.VIEW']

    for url in search_urls:
        subprocess.run(adb_command + ['-d', url])


def main():
    """
    Entry point of the program.
    """
    num_searches = int(input("Enter the number of searches: ")) or 20
    perform_searches(num_searches)


if __name__ == '__main__':
    main()
