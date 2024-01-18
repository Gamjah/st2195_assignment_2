from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Comma-separated_values"
data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

csv_raw = soup.findAll('pre')

csv_edited = csv_raw[10].text
print(csv_edited)

f = open("/Users/tiagooliveira/Dev/LSE/st2195_assignment_2/python_csv/carsdata.csv","w")

with open("/Users/tiagooliveira/Dev/LSE/st2195_assignment_2/python_csv/carsdata.csv","w") as f:
    f.write(csv_edited)

