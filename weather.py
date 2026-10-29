def Get_weather(City,Days):
  api_url="http://api.example.com/weather"
  full_url=api_url+"?city="+City+"&days="+str(Days)
  Unused_result = None
  print("Запрос погоды:",full_url)
  return full_url

X=Get_weather("Казань",3)
