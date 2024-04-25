import json
import requests
import sys


api_url = 'https://api.api-ninjas.com/v1/cars?limit=5&make=lamborghini&year=2024&model=urus'
api_url2 = 'https://api.api-ninjas.com/v1/cars?limit=5&make=toyota&'
api_url3 = 'https://api.api-ninjas.com/v1/cars?limit=5&make=toyota&year=2020'

response = requests.get(api_url, headers={'X-Api-Key': '+LNP8mg1hDCqYaUM+C6ElQ==xZ3S7GJWP3oQZBvU'})
# print(json.dumps(response.json(), indent=2))

def displayMenu():
    print("Welcome to the Car Information Hub. Search Whatever you would like.")

    while True:
        makeInput = input("Enter make: ")
        if makeInput == "Toyota":
            makeResponse = requests.get(api_url2, headers={'X-Api-Key': '+LNP8mg1hDCqYaUM+C6ElQ==xZ3S7GJWP3oQZBvU'})
            print(json.dumps(makeResponse.json(), indent=2))
            print("These are some of our", makeInput + "'s")
            optionResponse = input("Would you like to refine your search with a specific year or model? Enter Y to specify year, M to specify model. ")
            if optionResponse == "Y".upper():
                yearInput = input("Enter year of Toyota model: ")
                if yearInput == "2020":
                    yearResponse = requests.get(api_url3, headers={'X-Api-Key': '+LNP8mg1hDCqYaUM+C6ElQ==xZ3S7GJWP3oQZBvU'})
                    print(json.dumps(yearResponse.json(), indent=2))
                    print("Here are some", yearInput + " " + makeInput + "'s.")
                    break
        else:
            print("Invalid make.")
        

def main():
    displayMenu()

if __name__ == "__main__":
    main()