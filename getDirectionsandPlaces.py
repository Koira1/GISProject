import requests
import json

def getLocations(url):
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    routes = json.loads(response.text)
    i = 0
    listofdestinations = []
    if(bool(routes["routes"])):
        if(bool(routes["routes"][0]["legs"])):
            if(bool(routes["routes"][0]["legs"][0]["steps"])):
                while i < len(routes["routes"][0]["legs"][0]["steps"]):
                    temp = routes["routes"][0]["legs"][0]["steps"][i]['end_location']
                    listofdestinations.append(temp)
                    i = i + 1
                route = { "route" : listofdestinations }
                write_json(route)
            else:
                print(response.text)
                print("No steps found")
        else:
            print(response.text)
            print("No legs found")
    else:
        print(response.text)
        print("No route found")
        

def getHotels(url):
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    hotels = json.loads(response.text)
    listofhotels = []
    i = 0
    while i < len(hotels["results"]):
        data = {
        "location" : hotels["results"][i]["geometry"]["location"],
        "name" : hotels["results"][i]["name"]
        }
        listofhotels.append(data)
        i = i + 1

    hoteldata = { "hotels": listofhotels }
    write_json(hoteldata)

# function to add to JSON
def write_json(new_data, filename='hotels.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["data"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

f = open('data.json')

#data = json.load(f)

data = json.load(f)

i = 0
origin = {}
destination = {}

while i < len(data["data"]) - 1:
    origin = json.loads(data["data"][i])
    #destination = json.loads(data["data"][i+1])
    #url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + str(origin['latitude']) + "," + str(origin['longitude']) + "&destination=" + str(destination['latitude']) + "," + str(destination['longitude']) + "&key="
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(origin['latitude']) + "," + str(origin['longitude']) + "&radius=5000&type=hotel&key="
    #print(i)
    #getLocations(url)
    getHotels(url)
    i = i + 1
    

f.close()


#url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=41.013888888888886,28.955555555555556&radius=5000&type=hotel&key="
#getHotels(url)
#getLocations(url)


