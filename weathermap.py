#######################################################
############ Name : Sheryl Muthoni######################
############  Date : 14 / 06 / 2022 ####################

import requests, json

BASE_URL ="https: // api.openweathermap.org/data/2.5/weather?"
City= input("Enter The city of your choice ")
API_KEY = "baab46c0cc3e0d2c177b6f2c892cf93d"
URL =BASE_URL + "q="+ City + "&aapid="+API_KEY

response = requests.get(URL)

if response.status_code ==200:
    data =response.json()
    main = data['main']
    temperature= main['temp']
    humidity=main['humidity']
    pressure=main['pressure']
    report = data ['weather']
    print(f"{City:^30}")
    print(f"humidity{humidity}")
    print(f"pressure{pressure}")
    print(f"weather report{report[0]['description']}")

else:
    print("Error in the Http request please try again")



