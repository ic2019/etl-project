# Importing libraries
# Dependencies
import pandas as pd
import numpy as np
import requests
import json
from pprint import pprint
# Google API Key
from config import *
import re
import unidecode

# Reading restaurant csv into a pandas dataframe
# Reading the restaurant data
def read_data(file_path):
    """
    Function to read csv
    parameters : file_path
    Return: pandas dataframe
    """
    restaurant = pd.read_csv(file_path, doublequote=True)
    return restaurant

# Querying Google API to gather restaurant name, rating and price levels**
def get_from_api():
    """
    Function to query google API and gather data for al restaurants
    parameters : None
    Return: pandas dataframe
    """
    restaurant = read_data("./../Resources/restaurant.csv")
    # Setting up additional columns to hold data
    restaurant['rating'] = ""
    restaurant['name'] = ""
    restaurant["price_level"] = ""
    # Gathering restaurant info and rating for that latitude and logitude
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    params = {
        "ranking": "prominence",
        'type': 'restaurant',
        'keyword': 'pizza',
        "key": gkey
        }

    # use iterrows to iterate through pandas dataframe
    for index, row in restaurant.iterrows():

        params['query'] = f"{row['address']}, &{row['city']}, &{row['state']} &{row['zip_code']}, USA"
        params['location'] = row['latitude'],row['longitude']

    # assemble url and make API request

        address = f"{row['address']}, {row['city']}, {row['state']} {row['zip_code']}, USA"

        response = requests.get(base_url, params=params).json()


        try:
             # extract results
            results = response['results']
            # pprint(results)
            for result in results:
            
                if re.search(address, result['formatted_address']):
                    print(f"Address: {result['formatted_address']} Name: {result['name']} Rating: {result['rating']} Price Level: {result['price_level']}")
                    restaurant.loc[index, 'name'] = result['name']
                    restaurant.loc[index, 'rating'] = result['rating']
                    restaurant.loc[index, "price_level"] = result['price_level']
                    print("------------")

        except (KeyError, IndexError):
            print("Missing field/result... skipping.")
    return restaurant

def get_best_from_api():
    """
    Function to query google API and gather data for al restaurants
    parameters : None
    Return: pandas dataframe
    """
    # Reading best restaurant data into a csv
    best_restaurants = read_data("./../Resources/best_pizza_stores.csv")
    # Initializing dataframe columns
    best_restaurants['rating'] = ""
    best_restaurants['address'] = ""
    best_restaurants["price_level"] = ""
    best_restaurants["zip_code"] = ""
    
    # Gathering restaurant info and rating for that latitude and logitude


    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    params = {
        "ranking": "prominence",
        "type": "restaurant",
        "keyword": "pizza",
        "key": gkey
}

    # use iterrows to iterate through pandas dataframe
    for index, row in best_restaurants.iterrows():
        r_name = unidecode.unidecode(row['restaurant_name'])
        params['query'] = f"{r_name}&, {row['city']}&, {row['state']}&USA"

        # assemble url and make API request
        response = requests.get(base_url, params=params).json()

        try:
            # extract results
            results = response['results']
            for result in results:

                #if re.search(r_name,result['name']):
                print(f"Address: {result['formatted_address']} Name: {result['name']} Rating: {result['rating']} Price Level: {result['price_level']}")
                best_restaurants.loc[index, 'address'] = result['formatted_address'].split(',')[0]
                best_restaurants.loc[index, 'rating'] = result['rating']
                best_restaurants.loc[index, "price_level"] = result['price_level']
                best_restaurants.loc[index, "zip_code"] = result['formatted_address'].split(',')[2].split()[1]
                print("------------")
                break
     
        except (KeyError, IndexError):
            print("Missing field/result... skipping.")
    return best_restaurants