#This File will be used to scrape files from the classes.uwaterloo page
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://classes.uwaterloo.ca/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')