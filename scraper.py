# ============================================
# Projet : Scraping + ML - Prix Smartphones
# ============================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scraper_gsmarena(url):
    """Scrape les données d'un smartphone sur GSMArena"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extraire_specs(soup):
    """Extrait les spécifications du smartphone"""
    specs = {}
    
    # Nom du téléphone
    try:
        specs['nom'] = soup.find('h1', class_='specs-phone-name-title').text.strip()
    except:
        specs['nom'] = 'N/A'
    
    # Spécifications
    tables = soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == 2:
                key = cells[0].text.strip()
                value = cells[1].text.strip()
                specs[key] = value
    
    return specs

# Test avec un smartphone
print("Scraper initialisé ✅")
print("Prêt à scraper les données...")