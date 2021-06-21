import requests
from datetime import datetime

def Data_into_File(DATA):
	with open("Weather_Report.txt" , "a") as file:
		file.write(DATA)


api_key = '38bf87d003776a3e52dd32d80ab16b5b'
print(">>>>>>>>>>>>> Weather_Report <<<<<<<<<<<<<")
while(True):
	location = input("Enter the city name: ")
	try:
		complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
		api_link = requests.get(complete_api_link)
		api_data = api_link.json()

		#create variables to store and display data
		temp_city = ((api_data['main']['temp']) - 273.15)
		weather_desc = api_data['weather'][0]['description']
		hmdt = api_data['main']['humidity']
		wind_spd = api_data['wind']['speed']
		date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

		DATA_REP = ("\n-------------------------------------------------------------\n")
		DATA_REP+=str("Weather Stats for - {}  || {}".format(location.upper(), date_time))
		DATA_REP+= ("\n-------------------------------------------------------------\n")

		DATA_REP+= str("Current temperature is: {:.2f} deg C\n".format(temp_city))
		DATA_REP+= str("Current weather desc  :"+str(weather_desc)+"\n")
		DATA_REP+= str("Current Humidity      :"+str(hmdt)+ '%\n')
		DATA_REP+= str("Current wind speed    :"+str(wind_spd)+ 'kmph\n')
		print (DATA_REP)
		print(">>>> data is saved in ''Weather_Report.txt''")
		print("\n\n>>>>> press ctrl+z to exit\n\n")
		Data_into_File(DATA_REP)
	except Exception:
		print("city name might not be correct, please try again")
		continue
