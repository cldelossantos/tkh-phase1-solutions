from bs4 import BeautifulSoup
import requests
import csv

def percentage_converter(float):
    
    percentage = float * 100
    return f"{'{0:.2f}'.format(percentage)}%"

def scraping_covid_data():
    r = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data')
    soup = BeautifulSoup(r.text)
    covid_data = [['country', 'cases', 'deaths', 'recoveries', 'death_rate', 'recovery_rate']]
    for row in soup.select('tr')[2:]:
        try:
            country_name = list(row.select('th')[1].strings)[0]

            country_cases = list(row.select('td')[0].strings)[0][:-1]
            if country_cases == 'No dat':
                country_cases = None

            country_deaths = list(row.select('td')[1].strings)[0][:-1]
            if country_deaths == 'No dat':
                country_deaths = None

            country_recovery = list(row.select('td')[2].strings)[0][:-1]
            if country_recovery == 'No dat':
                country_recovery = None

            country_death_rate = None
            country_recovery_rate = None

            if country_deaths and country_cases:
                country_death_rate = percentage_converter(int(country_deaths.replace(',',''))/int(country_cases.replace(',',''))) 

            if country_recovery and country_cases:
                country_recovery_rate = percentage_converter(int(country_recovery.replace(',',''))/int(country_cases.replace(',','')))

            country_data = [country_name, country_cases, country_deaths, country_recovery, country_death_rate, country_recovery_rate]
            covid_data.append(country_data)  
        except:
            break 

    return covid_data

if __name__ == '__main__':
    output_to_file = open('Claudia-DeLosSantos-covid-report.csv', 'w')
    writefile = csv.writer(output_to_file)
    writefile.writerows((scraping_covid_data()))
    output_to_file.close()
    