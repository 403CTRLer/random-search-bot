import subprocess
import random
import string

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def open_edge():
    """
    Opens Microsoft Edge using the subprocess module.
    """
    subprocess.Popen([EDGE_PATH])


def generate_random_query(length=10):
    """
    Generates a random search query of specified length.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def perform_searches(num_searches):
    """
    Performs a specified number of searches with random queries using Microsoft Edge.
    """
    urls = [
        f"https://www.bing.com/search?q={generate_random_query()}" for _ in range(num_searches)]
    subprocess.Popen([EDGE_PATH] + urls)


# Open Microsoft Edge
open_edge()

# Perform searches
num_searches = int(input("Enter the number of searches: ")) or 30
perform_searches(num_searches)
