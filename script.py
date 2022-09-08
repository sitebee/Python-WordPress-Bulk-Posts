"""Python WordPress Bulk Posts v1.0.ipynb

This script: WordPress Bulk Posts v1.0 - Bulk upload Wordpress posts from CSV files via WordPress Rest API. The CSV files can be uploaded via Google Colab or fetched from a remote location (upload from Google sheets coming in the next version).
"""

# Import modules
import pandas as pd
import requests
import csv
import json
import base64
from tqdm.notebook import tqdm

# WordPress Rest API credentials
user = 'admin'
password = 'kJid Xqyu d7K9 fRmK 7cfN d8c6'
url = 'https://airwolf.dev/wp/wp-json/wp/v2'

wp_connection = user + ':' + password

token = base64.b64encode(wp_connection.encode())

# Base64 Authentication WordPress
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

from google.colab import files
uploaded = files.upload()

# Paste your uploaded csv file name here - example: sample-data.csv or paste remote web link
df = pd.read_csv("https://airwolf.dev/wp/sample_posts.csv")
df

# WP_Post_Insert Function to build the JSON array
# (add or remove post schemas to suit your requirements)
def wp_post_insert(post_title, post_content):

    post = {'title': post_title,
            'status': 'publish',
            'content': post_content,
            'author': '1',
            'format': 'standard'
            }

    wp_post_insert_request = requests.post(url + '/posts', headers=headers, json=post)

# Executes the script and runs the TQDM progress bar
for index, row in tqdm(df.iterrows()):
# Add or remove WordPress post schemas varibles below
    wp_post_insert(row["post_title"], row["post_content"])
