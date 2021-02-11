import random
from bs4 import BeautifulSoup
import requests
#Simple chat program
#Responds randomly with one of four preprogrammed responses

def generic_response(user_input):
  responses = [
    "How interesting!",
    "Good to know",
    "Very cool!",
    
  ]
  return random.choice(responses)
def hobbies(user_input):
  global choice_topic
  user["hobbies"]= input(user["name"] +", what is your favorite hobby?\n")
  print("Huh, I've never tried "+user["hobbies"]+" before.\n")
  user_input=input("How often do you perform "+user["hobbies"]+"?\n")
  generic_response(user_input) 
  print("I typically stay inside all day.")
  user["hobbies"]=input("Have you picked up any new hobbies due to the pandemic?\n")
  generic_response(user_input)
  print("During the pandemic I've been practicing my coding skills.")
  choice_topic=input(user["name"]+", what else would you like to talk about?\n")

#def family(user_input):
#  pass
def weather(user_input):
  weather_page=requests.get("https://weather.com/weather/today/l/d15df4c2c0efd911595f6df096c22c42ae65e3666f3eb406d7a15adcfef60a07")
  soup= BeautifulSoup(weather_page.content,'html.parser')



def food(user_input):
  user["food"]=input("What is your favorite food?\n") 
  generic_response(user_input)
  cook=input("Do you prefer to cook your own food or go to a restaurant?\n") 
  if "cook" in cook.capitalize():
    pass
  elif "restaurant" in cook.capitalize():
    pass

def school(user_input):
  global choice_topic
  user["grade"]=input("What grade are you in?\n")
  if int(user["grade"])<9:
    print("You should definitely check out Code2College when you get to high school.")
  elif 9<= int(user["grade"])<12:
    user_input=input("Are you involved with Code2College?\n")
    if "Yes" in user_input.capitalize():
      user["c2c"]=True
      interests=input("What do you like about Code2College?\n")
      print("Me too!")
      user_input="No"
    elif "No" in user_input.capitalize():
      user["c2c"]=False
      interests=input("What do you like about school?\n")
      user_input=input("Do you think you'll want to study that in college or make a career out of it?\n")
  elif user["grade"]>=12:
    user["college"]=input("What college are you going to?\n ")
    print(user["college"]+" is quite the prestigious university")
    interests=input("What is your major?")
    print("Sounds like you'll have an illustrious career!")
    choice_topic=input("What would you like to talk about next?\n ")

user={
"name":'',
"grade":'',
"hobbies":'',
"food":'',
#"brothers":'',
#"sisters":'',
#"parents":'',
"c2c":'',
"college":'',


}

def init_chat():
  
  quit_character = 'q'
  user_input=''
  
  user["name"]=input("Hello, what is your name?\n")
  print("Hello "+user["name"]+"\n")
  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    topics=" Hobbies\n Food\n School" 
    print(topics)
    choice_topic=input("What would you like to talk about?\n ")
    if choice_topic== "Hobbies":
      hobbies(user_input)
   # elif choice_topic == "Family":
     # family(user_input)
    elif choice_topic == "Food":
      food(user_input)
    elif choice_topic== "School":
      school(user_input)
  if user["c2c"]==True:
    print("Thanks for talking, good luck preparing for your internship.")
    

if __name__ == "__main__":
  init_chat()