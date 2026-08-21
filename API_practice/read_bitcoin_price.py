import requests
import pyttsx3

def main():
    price=get_price()
    print(f"bitcoin's current price is {price}$")
    read_price(price)

def get_price():
    # API Request
    response=requests.get("https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&x_cg_demo_api_key=CG-hWWLrcbH87u3ZDr5szfy9HLF")

    # get info in json format
    info=response.json()
    # return current price
    return info["bitcoin"]["usd"]

def read_price(p):
    # read with texttospeech feature
    engine = pyttsx3.init()
    engine.say(f"bitcoin's current price is {p}$")
    engine.runAndWait()


main()