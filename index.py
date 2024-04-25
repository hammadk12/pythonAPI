import json
import requests
import re


def displayMenu(make, model, year):
    
    api_url = f'https://api.api-ninjas.com/v1/cars?limit=30&make={make}&model={model}&year={year}'
    response = requests.get(api_url, headers={'X-Api-Key': '+LNP8mg1hDCqYaUM+C6ElQ==xZ3S7GJWP3oQZBvU'})

    if response.status_code == 200:
        data = response.json()
        if data: # Check if data list is not empty
            print("Vehicles: ")
            print(json.dumps(response.json(), indent=2))
            search_more()    
        else:
            print("No matches found.")
            make, model, year = get_car_info() # reprompt for input
            displayMenu(make, model, year) # recursive call with NEW input
    else:
        print("Failed to retrieve data. Please check your inputs.")
    
# another search function
def search_more():
    while True:
        search = input("Would you like to perform another search? (Y/N) ")
        if search == "Y".upper():
            make, model, year = get_car_info() # reprompt for input
            displayMenu(make, model, year)
        elif search == "N".upper():
            print("Have a nice day! Thank you for using the Car Information Hub :)")
            break
        else:
            print("Invalid input, please select (Y/N)")

# validate make input
def get_valid_make(prompt):
    while True:
        make_input = input(prompt)

        if re.match(r"^[A-Za-z ]+$", make_input):
            return make_input
        else:
            print("Invalid make. Please enter valid make, only letters.")

# validate model input
def get_valid_model(prompt):
    while True:
        model_input = input(prompt)

        if re.match(r"^[A-Za-z0-9]+$", model_input):
            return model_input
        else:
            print("Invalid model. Please enter a valid model using only letters and numbers.")

# validate year input
def get_valid_year(prompt):
    while True:
        year_input = input(prompt)

        if re.match(r"^[0-9]+$", year_input):
            year = int(year_input)
            if year >= 1980:
                return year
            else:
                print("Invalid year. Please enter a year starting from 1980.")
        else:
            print("Invalid year. Please enter valid year with only numbers.")


def get_car_info():
    print("Welcome to the Car Information Hub. Search Whatever you would like.")
    make = get_valid_make("Enter make: ")
    model = get_valid_model("Enter model: ")
    year = get_valid_year("Enter year: ")
    return make, model, year

if __name__ == "__main__":
    make, model, year = get_car_info()    
    displayMenu(make, model, year)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if makeInput == "Toyota":
           # makeResponse = requests.get(api_url2, headers={'X-Api-Key': '+LNP8mg1hDCqYaUM+C6ElQ==xZ3S7GJWP3oQZBvU'})
            #print(json.dumps(makeResponse.json(), indent=2))
            #print("These are some of our", makeInput + "'s")
            #optionResponse = input("Would you like to refine your search with a specific year or model? Enter Y to specify year, M to specify model. ")
            #if optionResponse == "Y".upper():
                #yearInput = input("Enter year of Toyota model: ")
                #if yearInput == "2020":
                    #yearResponse = requests.get(api_url3, headers={'X-Api-Key': '+LNP8mg1hDCqYaUM+C6ElQ==xZ3S7GJWP3oQZBvU'})
                    #print(json.dumps(yearResponse.json(), indent=2))
                    #print("Here are some", yearInput + " " + makeInput + "'s.")
                    #break
        #else:
            #print("Invalid make.")