#Virus Simulator version 3
#25/11/2021
#Aaron Sharma

#To enhance the user experience by managing how text is displayed.
import time
import sys
#welcome message
time.sleep(.75)
print("Welcome to the Pap High Virus Simulator\n Please follow the prompts")


#To store and track user input
country_list = []
num_infected = []
max_length_list = 3

name_country = ""

while len(name_country) < max_length_list:
  name_country = str(input("Please enter a country name")).upper()
  country_list.append(name_country)
  infected_percent = int(input("Please enter the number infected"))
  num_infected.append(infected_percent)

print(country_list,"is the country and ", num_infected, "is the amount infected")

def print_details(self):
  details = "" + self.name_country + "currently has " + str(self.infected_percent) + "percent infected, and "
  if self.is_in_lockdown == True:
    details += "is in lockdown"