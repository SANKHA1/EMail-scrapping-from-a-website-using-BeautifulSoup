import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd

# read url from input
original_url = input("Enter the website url: ")

# to save urls to be scraped
unscraped = deque([original_url])

# to save scraped urls
scraped = set()

# to save fetched emails
emails = set()