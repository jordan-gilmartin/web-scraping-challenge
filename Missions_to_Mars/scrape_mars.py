from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/webdrivers/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)


def scrape_info():

    # Begin scrape with Requests
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object and parse with html.parser
    soup = bs(response.text, 'html.parser')
    
    # Retrieve the latest News Title
    title = soup.find('div', class_='content_title').text.strip()
    
    # Retrieve the latest Paragraph Text
    p = soup.find('div', class_='rollover_description_inner').text.strip()


    # Begin scrape with Splinter - JPL Website
    # Instantiate the browser
    browser = init_browser()

    # Visit JPL website
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Click 'FULL IMAGE' upon arrival to access correct URL
    browser.links.find_by_partial_text('FULL IMAGE').click()

    # Load html
    html = browser.html

    # Create BeautifulSoup object and parse with html.parser
    soup = bs(html, 'html.parser')

    # Grab URL for photo
    jpl = soup.find('div', class_='fancybox-inner')
    src = jpl.img['src']

    # Combine to make full URL to photo
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/' + src


    # Grab table info
    # Read table from website into Pandas
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)

    # Grab first table
    df = tables[0]

    # Rename columns
    df.columns = ['Description', 'Mars']

    # Set index to description
    dfD = df.set_index('Description')

    # Create html file
    table = dfD.to_html(classes="table table-striped")


    
    # Scrape with Splinter - Cerberus
    # Head to website to grab photo and title
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Click 'Cerberus' upon arrival to access next page for title
    browser.links.find_by_partial_text('Cerberus').click()

    # Load html
    html = browser.html

    # Create BeautifulSoup object and parse with html.parser
    soup = bs(html, 'html.parser')    

    # Grab title of photo    
    cerbTitle = soup.find('h2', class_='title').text    

    # Grab URL of photo    
    cerbURL = soup.find('div', class_='downloads').a['href']
    
    
    # Scrape with Splinter - Schiaparelli 
    # Head to website to grab photo and title
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # click 'Schiaparelli' upon arrival to access next page for title
    browser.links.find_by_partial_text('Schiaparelli').click()

    # Load html
    html = browser.html   

    # Create BeautifulSoup object and parse with html.parser
    soup = bs(html, 'html.parser') 

    # Grab title of photo
    schiaTitle = soup.find('h2', class_='title').text    

    # Grab URL of photo
    schiaURL = soup.find('div', class_='downloads').a['href']
    


    # Scrape with Splinter - Syrtis 
    # Head to website to grab photo and title
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # click 'Syrtis' upon arrival to access next page for title
    browser.links.find_by_partial_text('Syrtis').click()

    # Load html
    html = browser.html

    # Create BeautifulSoup object and parse with html.parser
    soup = bs(html, 'html.parser')    

    # Grab title of photo    
    syrtTitle = soup.find('h2', class_='title').text    

    # Grab URL of photo
    syrtURL = soup.find('div', class_='downloads').a['href']
    


    # Scrape with Splinter - Valles Marineris 
    # Head to website to grab photo and title
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # click 'Valles Marineris' upon arrival to access next page for title
    browser.links.find_by_partial_text('Valles Marineris').click()

    # Load html
    html = browser.html

    # Create BeautifulSoup object and parse with html.parser
    soup = bs(html, 'html.parser')    

    # Grab title of photo    
    valsTitle = soup.find('h2', class_='title').text    

    # Grab URL of photo
    valsURL = soup.find('div', class_='downloads').a['href']


    # Save to List of Dictionaries
    hemisphere_image_urls = [
        {"title": valsTitle, "img_url": valsURL},
        {"title": cerbTitle, "img_url": cerbURL},
        {"title": schiaTitle, "img_url": schiaURL},
        {"title": syrtTitle, "img_url": syrtURL},
    ]

    # Dictionary to hold all values
    output = {
        "title": title,
        "p": p,
        "featured_image_url": featured_image_url,
        "table": table,
        "hemisphere_image_urls": hemisphere_image_urls,
    }


    # Close the browser after scraping
    browser.quit()

    # Return results
    return output
    









    # # Get the average temps
    # avg_temps = soup.find('div', id='weather')

    # # Get the min avg temp
    # min_temp = avg_temps.find_all('strong')[0].text

    # # Get the max avg temp
    # max_temp = avg_temps.find_all('strong')[1].text

    # # BONUS: Find the src for the sloth image
    # relative_image_path = soup.find_all('img')[2]["src"]
    # sloth_img = url + relative_image_path

    # # Store data in a dictionary
    # costa_data = {
    #     "sloth_img": sloth_img,
    #     "min_temp": min_temp,
    #     "max_temp": max_temp
    # }

    # # Close the browser after scraping
    # browser.quit()

    # # Return results
    # return costa_data



