import re
import requests
from bs4 import BeautifulSoup

from utils import format_date

# Ministry of Health(MOH)'s webpage for COVID-19 related news
MOH_COVID_URL = 'https://www.moh.gov.sg/covid-19'

# Prefix of URL for posts containing daily COVID-19 data.
START_OF_URL = "https://www.moh.gov.sg/news-highlights/details/"

# Suffix of URL for posts containing daily COVID-19 data.
END_OF_URL = "new-cases-of-covid-19-infection"

def get_soup_from_url(url: str) -> BeautifulSoup:
    """
    Gets `BeautifulSoup` object from URL of webpage.
    """
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')

def extract_data_from_post(soup: BeautifulSoup) -> dict:
    """
    Extract relevant data from the post's `BeautifulSoup` object.
    """
    results = soup.find('div', class_="columns large-12 no-padding").findAll("p", limit=2)
    for result in results:
        print(result)
    assert(len(results) == 2)

    date = format_date(re.compile('As of (.*?),').search(results[0].getText()).groups()[0])
    num_new = int(re.compile('additional ([0-9]*?) (?:case|cases) of COVID-19 infection in Singapore').search(results[0].getText()).groups()[0])
    num_imported = int(re.compile('there (?:are|is) ([0-9]*?) imported').search(results[0].getText()).groups()[0])
    num_community = int(re.compile('there (?:is|are) ([0-9]*?) (?:cases|case) in the community').search(results[0].getText()).groups()[0])
    num_dormitories = num_new - num_imported - num_community
    
    print(f"Date: {date}")    
    print(f"Number of cases in community: {num_community}")
    print(f"Number of cases in dormitories: {num_dormitories}")
    print(f"Number of imported cases: {num_imported}")
    print(f"Number of new cases: {num_new}")
    
    return {"date": date, "num_dormitories": num_dormitories, 
            "num_community": num_community, "num_imported": num_imported}

def get_post_url(soup: BeautifulSoup) -> str:
    """
    Get URL of latest post containing daily COVID-19 data.
    """
    def f(href):
        return href and href.startswith(START_OF_URL) and href.endswith(END_OF_URL)
    return soup.find(href=f)['href']
