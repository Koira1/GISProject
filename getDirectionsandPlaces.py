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
        


# function to add to JSON
def write_json(new_data, filename='directions.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["directions"].append(new_data)
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
    destination = json.loads(data["data"][i+1])
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + str(origin['latitude']) + "," + str(origin['longitude']) + "&destination=" + str(destination['latitude']) + "," + str(destination['longitude']) + "&key=AIzaSyCRQFrcOTRUAucq5FYDOg8beeE5ymI4uew"
    print(i)
    getLocations(url)
    i = i + 1
    

#for i in data[0]['location']:
#    print(i)

f.close()


#url = "https://maps.googleapis.com/maps/api/directions/json?origin=42.874722222222225,74.61222222222221&destination=40.53,72.8&key=AIzaSyCRQFrcOTRUAucq5FYDOg8beeE5ymI4uew"
#getLocations(url)


