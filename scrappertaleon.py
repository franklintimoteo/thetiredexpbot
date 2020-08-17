from functools import lru_cache
from typing import Generator

from bs4 import BeautifulSoup
import requests

#UNICODE PRIMEIRO | SEGUNDO | TERCEIRO
UNICODE_TROPHY = (u"\U0001f3c5", u"\U0001f948", u"\U0001f949")

#aplicar buscar em cima da tag a atributo href characterprofile.php?name=
@lru_cache()
def get_document_html(url, **kwargs):
    html_doc = requests.get(url, **kwargs)
    return html_doc


def get_soup_parser(url, **kwargs):
    html_doc = get_document_html(url, **kwargs)
    soup = BeautifulSoup(html_doc.content, "html5lib")
    return soup


def get_list_characters():
    """
    return: list members [str, str, ...]
    """
    soup = get_soup_parser("https://san.taleon.online/guilds.php?name=The%20Tired")
    raw_members = soup.find("div", attrs={"id": "tab1"})
    members = (member.text for member in raw_members.find_all("a"))
    return members


def get_experience_today(soup):
    table_children = soup.find("table")
    sibling_table = table_children.find_next_sibling("table")
    experience_today = sibling_table.tbody.td.next_element.next_element.text
    return experience_today


def get_experience_members_today():
    experience_members = {} # {"name": "14,000,00"}

    members = get_list_characters()

    for member in members:
        params = {"name": member}
        member_html_parser = get_soup_parser(f"https://san.taleon.online/characterprofile.php", params=params)
        experience_today = get_experience_today(member_html_parser)
        experience_members[member] = experience_today
    
    return experience_members
