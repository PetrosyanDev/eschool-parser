from . import console

import os

from bs4 import BeautifulSoup

def parseWeek(html: str) -> list:
    # GETTING URL
    url = os.getenv('BASE_URL')

    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # FIND ALL DAYLY TABLES
    all_tbody = soup.find_all('tbody')
    result = []

    for tbody in all_tbody:
        day = []

        # ITERATE THROUGH EACH TABLE
        for row in tbody.find_all('tr'):

            data = {}

            # EXTRACT TIME
            if row.find(class_='time'):
                data['time'] = row.find(class_='time').text.strip()

            # EXTRACT CLASS NAME AND URL
            if row.find(class_='class'):

                # IF HAS URL
                if row.find(class_='class').a:
                    data['class'] = url + row.find(class_='class').a['href']

                # CLASS NAME
                data['class_name'] = row.find(class_='class').text.strip()
            
            # EXTRACT MARKS
            if row.find(class_='marks'):
                data['marks'] = row.find(class_='marks').text.strip()

            # ADD TO DAY
            day.append(data)

        # ADD DAY TO WEEK
        result.append(day)
    
    console.console_log(f"Parsed {len(result)} days.")

    return result