import requests
import json
from datetime import datetime

def get_licenses():
    # The API endpoint
    url = "http://localhost:30000/drivers-licenses/list"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    return response_json

def list_suspended_licenses():
    obj = get_licenses()
    output_file = open("SuspendedLicenses.csv", 'w', encoding='utf-8')
    for item in obj:
        if item["suspendat"]:
            print(item)
            json.dump(item, output_file) 
            output_file.write("\n")

def list_valid_licenses():
    obj = get_licenses()
    output_file = open("ValidLicenses.csv", 'w', encoding='utf-8')
    for item in obj:
        datetimelicence = datetime.strptime(item["dataDeExpirare"], "%d/%m/%Y")
        if not item["suspendat"] and datetimelicence > datetime.now():
            print(item)
            json.dump(item, output_file) 
            output_file.write("\n")

def list_by_category():
    obj = get_licenses()
    output_file = open("CategoryByCount.csv", 'w', encoding='utf-8')
    a=a1=b=b1=c=c1=d=d1=c1e=be=de=d1e=0
    for item in obj:
        if item["categorie"] == "A":
            a=a+1
        elif item["categorie"] == "A1":
            a1=a1+1
        elif item["categorie"] == "B":
            b=b+1
        elif item["categorie"] == "B1":
            b1=b1+1
        elif item["categorie"] == "C":
            c=c+1
        elif item["categorie"] == "C1":
            c1=c1+1
        elif item["categorie"] == "D":
            d=d+1
        elif item["categorie"] == "D1":
            d1=d1+1
        elif item["categorie"] == "C1E":
            c1e=c1e+1
        elif item["categorie"] == "BE":
            be=be+1
        elif item["categorie"] == "DE":
            de=de+1
        elif item["categorie"] == "D1E":
            d1e=d1e+1
    print('A=>', a, 'A1=>', a1, 'B=>', b, 'B1=>', b1, 'C=>', c, 'C1=>', c1, 'D=>', d, 'D1=>', d1, 'C1E=>', c1e, 'BE=>', be, 'DE=>', de, 'D1E=>', d1e)
    mesaj='A=>', a, 'A1=>', a1, 'B=>', b, 'B1=>', b1, 'C=>', c, 'C1=>', c1, 'D=>', d, 'D1=>', d1, 'C1E=>', c1e, 'BE=>', be, 'DE=>', de, 'D1E=>', d1e
    json.dump(mesaj, output_file) 
    output_file.write("\n")


if __name__ == '__main__':
    inp = input("Choose operation:\n 1 - For suspended licenses;\n 2 - For valid licenses;\n 3 - For category count: \n")
    if inp == "1":
        print("Suspended licences: ")
        list_suspended_licenses()
    if inp == "2":
        print("Valid Licenses: ")
        list_valid_licenses()
    if inp == "3":
        print("Category count: ")
        list_by_category()
    ext=input("press enter to exit")
