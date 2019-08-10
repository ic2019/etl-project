# Scraping Data for Best Pizza Stores.
# Importing Libraries

from bs4 import BeautifulSoup
import pandas as pd
import requests
from splinter import Browser
import time
import json
import re

# Initializing Functions
# Defining functions to instantiate webdriver, opening browser and closing browser.

def init_browser():
    """
    Function to create an instance of Chrome webdriver class object.
    Parameters: None
    Return: browser object
    """
    # Import Splinter and set the chromedriver path
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    return browser

def open_browser(browser, url):
    """
    Function to open the url using the browser instance of Chrome webdriver class object.
    Parameters: browser object and url of the web page.
    Return: None
    """
    browser.visit(url)

def close_browser(browser):
    """
    Function to close the webpage opened using chromedriver object.
    Parameters: browser object
    Return: None
    """
    browser.quit()

# Gather html data using Splinter

# Use splinter to get the html page into an object
def scrape_best_pizza():
    """
    Function to extract the Daily Meal webpage into anhtml object using spinter and
    parse all the required data using beautifulsoup4.
    Parameters: None
    Return: A dictionary of all extracted data.
    """

    url = "https://www.thedailymeal.com/eat/best-pizza-every-state-slideshow"
    browser = init_browser()
    open_browser(browser, url)
    html = browser.html
    # Closing the browser
    close_browser(browser)

    # Scraping the best pizza stores details from the html object using bs4
    # Use bs4 to scrape the elemnets from the html object
    state = []
    name = []
    city = []
    # <div class="image-title slide-title"><h2>Alabama: Bottega Café (Birmingham)</h2></div>
    
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', {'class':'slide-main'})


    for item in results:
        state_string = item.find('div', {'class' : ['image-title', 'slide-title']}).find('h2').text
        try:
            pattern = re.compile(r'Washington, D.C')
            if re.match(pattern, state_string.split(':')[0]):
                continue
            else:

                #state.append(state_string.split(':')[0])
                state.append(str.strip(state_string.split(':')[0]))
                name.append(str.strip(state_string.split(':')[1].split('(')[0]))
                city.append(str.strip(state_string.split(':')[1].split('(')[1].split(')')[0]))
                print(f"{str.strip(state_string.split(':')[0])}---{str.strip(state_string.split(':')[1].split('(')[0])}---{str.strip(state_string.split(':')[1].split('(')[1].split(')')[0])}")
        except Exception as e:
            print(f"Skipping....")


        
    #print(f"{state} {name} {city}")

    # Creating a dataframe for state wise best pizzas
    best_pizza_stores = pd.DataFrame({'restaurant_name' : name,
        'city' : city,
      'state': state })


    return best_pizza_stores

