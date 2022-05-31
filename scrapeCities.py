from bs4 import BeautifulSoup
import requests
import re
import json

def convert(coordinate):
    coordinate = coordinate.replace("′", "\'")
    coordinate = coordinate.replace("″", "\"")
    if(len(re.split('[°\'"]', coordinate)) == 4):
        deg, minutes, seconds, direction =  re.split('[°\'"]', coordinate)
        coordinate = (float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * (-1 if direction in ['W', 'S'] else 1)
    else:
        deg, minutes, direction = re.split('[°\'"]', coordinate)
        coordinate = (float(deg) + float(minutes)/60) * (-1 if direction in ['W', 'S'] else 1)
    return coordinate

fp = requests.get("https://en.wikipedia.org/wiki/Cities_along_the_Silk_Road")

soup = BeautifulSoup(fp.text, "html.parser")

list = ['Turkey', 'Azerbaijan', 'Georgia', 'Armenia', 'Lebanon', 'Syria', 'Iraq', 'Iran', 'Turkmenistan', 'Uzbekistan', 'Tajikistan', 'Kazakhstan', 'Kyrgyzstan', 'Afganisthan', 'Pakistan', 'India', 'Nepal', 'Bangladesh', 'Bhutan', 'Korea', 'Japan']

li = soup.body.find_all('a')
i = 0
listOfWikies = []
keepindex = [30, 33, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 47, 48, 49, 51, 53, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80, 81, 82, 83, 84, 85, 86, 87, 89, 90, 91, 96, 98, 99, 100, 101, 102, 104, 107, 109, 111, 112, 113, 114, 120, 122, 123, 124, 125, 127, 128, 129, 131, 132, 134, 135, 136, 137, 138, 140, 143, 145, 146, 147, 148, 149, 151, 155, 156, 157, 158, 159, 160, 161, 164, 167, 170, 171, 184, 185, 186, 187, 188, 189, 190, 191, 194, 196, 197, 198, 199, 200, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 216, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 237, 238, 239, 240, 242, 243, 244, 245]
for a in li:
    if(str(a.get('href')).startswith('/wiki/')):
        if i in keepindex:
            listOfWikies.append("https://en.wikipedia.org" + a.get('href'))
        i = i + 1

y = []

for link in listOfWikies:
    fp = requests.get(link)
    soup = BeautifulSoup(fp.text, "html.parser")
    span1 = soup.body.find("span", {"class": "latitude"})
    span2 = soup.body.find("span", {"class": "longitude"})
    parsedlink = link[30:]
    if span1 is None:
        continue
    else:
        lat = convert(str(span1.text))
        long = convert(str(span2.text))
        print(parsedlink + " : " + "Latitude: " + str(lat) + ", Longitude: " + str(long))
        x = {
            "location": parsedlink,
            "latitude": lat,
            "longitude": long
        }
        y.append(json.dumps(x))
        
with open('data.json', 'w') as f:
    json.dump(y, f)

