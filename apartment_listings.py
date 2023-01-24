from bs4 import BeautifulSoup
import requests
import csv
import os

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
    url = requests.get('https://www.realtor.com/apartments/07109/beds-2')
    soup = BeautifulSoup(url.content, 'html.parser')
    listings = soup.find_all('div', class_= 'CardContent__StyledCardContent-rui__sc-7ptz1z-0 echMdB card-content')
    
    # Input each listing into a file
    for listing in listings:
        price = listing.find('div', class_= 'price-wrapper').text
        location = (
            f"{listing.find('div', attrs={'data-testid': 'card-address-1'}).text}"
            ", "
            f"{listing.find('div', attrs={'data-testid': 'card-address-2'}).text}"
        )
        
        bed = listing.find('li', class_= 'styles__StyledPropertyBedMeta-rui__jbdr1y-0 gUHOjr').text
        bath = listing.find('li', class_= 'styles__StyledPropertyBathMeta-rui__sc-6egb6z-0 dqxXcq').text

        # Some listings don't have area size or pet info readily available
        # Us try, except to handle missing attributes
        try:
            area = (
                listing.find('li', class_= 'styles__StyledPropertySqftMeta-rui__sc-1f5nqhv-0 hZvqmo')
                .find('span', class_='styles__StyledVisuallyHidden-rui__sc-1otsbow-0 kvJPgr').text
            )
        except AttributeError:
            area = "Info N/A"
        
        try:
            pets = (
                listing.find('li', class_= 'styles__StyledPropertyPetMeta-rui__sc-1ebu08q-0 bWZehQ')
                .find('span', class_= 'styles__StyledVisuallyHidden-rui__sc-1otsbow-0 kvJPgr').text
            )
        except AttributeError:
            pets = "Info N/A"
            
        
        info = [price, location, bed, bath, area, pets]
        

def find_redfin_listings():
    """Find apartments in Belleville, NJ on redfin.com"""
    url = requests.get('https://www.redfin.com/zipcode/07109/apartments-for-rent')
    soup = BeautifulSoup(url.content, 'html.parser')
    listings = soup.find_all('div', class_= 'MapHomeCardReact HomeCard')
    
    # Input each listing into a file
    for listing in listings:
        price = listing.find('span', class_= 'homecardV2Price').text
        location = listing.find('div', class_= 'homeAddressV2').text
        bed = listing.find('div', class_= 'HomeStatsV2 font-size-small').find_all('div', class_='stats')[0].text
        bath = listing.find('div', class_= 'HomeStatsV2 font-size-small').find_all('div', class_='stats')[1].text
        area = listing.find('div', class_= 'HomeStatsV2 font-size-small').find_all('div', class_='stats')[2].text
        if area == "—Sq. Ft.":
            area = "Info N/A"
                
        # Pet info is not readily available in Redfin, so '----' is just dummy text to trigger the try except
        try:
            pets = listing.find('div', class_= '----').text
        except AttributeError:
            pets = "Info N/A"

        redfin_info = [price, location, bed, bath, area, pets]

def find_zillow_listings():
    """Find apartments in Belleville, NJ on zillow.com"""
    url = se.get('https://www.zillow.com/homes/07109_rb/')
    soup = BeautifulSoup(url.content, 'html.parser')
    listings = soup.find_all('li', class_= 'ListItem-c11n-8-81-1__sc-10e22w8-0 srp__hpnp3q-0 enEXBq with_constellation')
    
    # Input each listing into a file
    for listing in listings:
        try:
         price = listing.find('div', class_= 'StyledPropertyCardDataArea-c11n-8-81-1__sc-yipmu-0 wgiFT').text
        except:
            continue

        location = listing.find('a', class_= 'StyledPropertyCardDataArea-c11n-8-81-1__sc-yipmu-0 lpqUkW property-card-link').text
        bed = (
            listing.find('ul', class_= 'StyledPropertyCardHomeDetailsList-c11n-8-81-1__sc-1xvdaej-0 cBiTXE')
            .find_all('li')[0].text
        )
        
        try:
            bath = (
                listing.find('ul', class_= 'StyledPropertyCardHomeDetailsList-c11n-8-81-1__sc-1xvdaej-0 cBiTXE')
                .find_all('li')[1].text
            )
        except:
            bath = "Info N/A"
        if "bds" in bath:
            bath = "Info N/A"
        
       
        try:
            area = (
                listing.find('ul', class_= 'StyledPropertyCardHomeDetailsList-c11n-8-81-1__sc-1xvdaej-0 cBiTXE')
                .find_all('li')[2].text
            )
        except:
            area = "Info N/A"
        if "--" in area:
            area = "Info N/A"
        
        # Pet info is not readily available in Zillow, so '----' is just dummy text to trigger the try except
        try:
            pets = listing.find('div', class_= '----').text
        except AttributeError:
            pets = "Info N/A"

        zillow_info = [price, location, bed, bath, area, pets]

