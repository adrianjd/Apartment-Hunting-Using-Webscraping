from bs4 import BeautifulSoup
import requests


def find_realtor_listings():
    """Find 2 bedroom apartments on realtor.com"""
    website = requests.get('https://www.realtor.com/apartments/07109/beds-2')
    soup = BeautifulSoup(website, 'html.parser')
    listings = soup.find_all('div', class_= 'CardContent__StyledCardContent-rui__sc-7ptz1z-0 echMdB card-content')
    
    # Input each listing into a file

def find_redfin_listings():
    """Find 2 bedroom apartments on redfin.com"""
    website = requests.get('https://www.redfin.com/zipcode/07109/apartments-for-rent')
    soup = BeautifulSoup(website, 'html.parser')
    listings = soup.find_all('div', class_= 'bottomv2')
    
    # Input each listing into a file

def find_zillow_listings():
    """Find 2 bedroom apartments on zillow.com"""
    website = requests.get('https://www.zillow.com/homes/07109_rb/')
    soup = BeautifulSoup(website, 'html.parser')
    listings = soup.find_all('li', class_= 'ListItem-c11n-8-81-1__sc-10e22w8-0 srp__hpnp3q-0 enEXBq with_constellation')
    
    # Input each listing into a file


