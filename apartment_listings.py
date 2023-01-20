from bs4 import BeautifulSoup
import requests


"""
realtor.com and redfin.com kept giving 403 error status codes. Used following code to fix.
For personal use: visit website, right-click inspect > network tab > click a GET request with
a '200' Status code > scroll down the newly-opened 'Headers' tab > copy the 'User-Agent' field and
replace here.
"""
with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
    }


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


