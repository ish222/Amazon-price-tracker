from bs4 import BeautifulSoup  # importing relevant libraries
import requests

url = "https://www.amazon.co.uk/Samsung-MZ-76E500B-EU-Solid-State/dp/B078WST5RK/ref=sr_1_1?dchild=1&keywords=samsung%2Bssd&qid=1604769725&sr=8-1&th=1"
# URL of Samsung SSD I am tracking the price of
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
# The line above just states the user agent of my browser which is required for the requests to work

page = requests.get(url, headers=headers) #Allows for a connection to the website

soup = BeautifulSoup(page.content, "html.parser") #Parses the website to obtain its information

price = (soup.find(id="priceblock_ourprice").get_text()).strip() #Finds the price by using the id obtained from using Inspect Element in Google Chrome and then returns its text
intprice = int(price[1:4]) #Only takes the first 3 digits of the price and converts them to integers

try: #Does error handling to catch value errors
    inputprice = int(input("What is your minimum price for the Samsung 1TB SSD?"))
except ValueError:
    print("You input a wrong value!")
    quit()

if intprice < inputprice: #Checks if the price is below the input price
    print(f"The price of the SSD has dropped below {inputprice}\nThe current price is ", intprice)
else:
    print(f"The price of the SSD has not dropped below {inputprice}\nThe current price is ", intprice)




