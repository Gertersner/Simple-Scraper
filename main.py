#provided imports
import requests, re
from bs4 import BeautifulSoup

#function for using agent vison and responding accordingly
def search():
  global temp, time, weather, wearResult
  
  #get the input from the user
  city = el1.get()
  
  #vison for this agent
  url = "https://www.google.com/search?q=weather" + city
  info = requests.get(url).content

  #scraping the data from the site
  look = BeautifulSoup(info, 'html.parser')
  temp = look.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
  str = look.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
  data = str.split('\n')
  time = data[0]
  weather = data[1]

  newTemp = int(re.compile("(\d+)").match(temp).group(1))

  #the large set of rules that the simple reflex agent refrences
  wearResult = "Unknown city"

  if newTemp > 80:
    wearResult = "wear shorts"
    if weather == ("Rain" or "Thunderstorm" or "Scattered thunderstorms"):
      wearResult = wearResult + " and bring an umbrella"
    elif weather == ("Sunny"):
      wearResult = wearResult + " and bring some sunscreen"
  elif newTemp > 65:
    wearResult = "wear short sleeves"
    if weather == ("Rain" or "Thunderstorm" or "Scattered thunderstorms"):
      wearResult = wearResult + " and bring an umbrella"
    elif weather == ("Sunny"):
      wearResult = wearResult + " and bring some sunscreen"
  elif newTemp > 45:
    wearResult = "wear fleece"
    if weather == ("Rain" or "Thunderstorm" or "Scattered thunderstorms"):
      wearResult = wearResult + " and bring an umbrella"
    elif weather == ("Sunny"):
      wearResult = wearResult + " and bring some sunscreen"
  elif newTemp > 25:
    wearResult = "wear a jacket"
    if weather == ("Rain" or "Thunderstorm" or "Scattered thunderstorms"):
      wearResult = wearResult + " and bring an umbrella"
    elif weather == ("Sunny"):
      wearResult = wearResult + " and bring some sunscreen"
  else:
    wearResult = "wear a winter coat"
    if weather == ("Rain" or "Thunderstorm" or "Scattered thunderstorms"):
      wearResult = wearResult + " and bring an umbrella"
    elif weather == ("Sunny"):
      wearResult = wearResult + " and bring some sunscreen"


#---------Start of GUI-----------#
from tkinter import *

#creates the user input screen
inputScreen = Tk()

inputScreen.title('Weather')
CityName = Label(inputScreen, text='City Name')
CityName.grid(row=0)

#creates the output that the user will see also seens as an "actuator"
def selected():

  city = el1.get()
  search()

  top = Toplevel()
  top.title('Weather Results for ' + city)
  top.geometry('400x100')

  heatEl = Label(top, text='The temperature is: ' + temp)
  timeEl = Label(top, text='Date and time is currently: ' + time)
  weatherEl = Label(top, text='The weather is: ' + weather)
  resultEl = Label(top, text='Recommendation is:  ' + wearResult)

  timeEl.grid(row=0)
  heatEl.grid(row=1)
  weatherEl.grid(row=2)
  resultEl.grid(row=3)


el1 = Entry(inputScreen)
el2 = Button(inputScreen, text='Enter', width=20, command=selected)
el1.grid(row=0, column=1)
el2.grid(row=2, column=1)

mainloop()