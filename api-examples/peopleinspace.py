#!/usr/bin/python
import requests
# Get a response from the API "endpoint".
response = requests.get("http://api.open-notify.org/astros.json")
# assign the json formated response to the variable "data"
data = response.json()

# we can now get the number "key" from data json
# this is a simple API with only two "keys" in the JSON response "number" and "people"
# so we will get the value from the number key and assign it to the people in space variable
peopleinspace = data["number"]

print(peopleinspace) # now print this

# or convert it to a string and join it with some other strings to make a sentence.
print("There are currently " + str(peopleinspace) + " people in space.")


for i in data["people"]:
    print i["name"]
