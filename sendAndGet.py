# Pratik Bharambe ................................

# Python code to send text data to Thingspeak.com cloud ......................
import urllib.request
def sendTextMessage(message):
    try:
        msg = message.replace(' ', "%20")
        msg = msg.replace('\n', "%0A")
        urllib.request.urlopen('https://api.thingspeak.com/update?api_key=7GMXR3PO7X34ZX58&field1=0' + msg)
        return True
    except:
        return False

# Python code to get text data from Thingspeak.com cloud ......................  
import requests
def getTextMessage():
    try:
        msg = requests.get("https://api.thingspeak.com/channels/2030745/feeds.json?results=2")
        msg = msg.json()['feeds'][-1]['field1']
        return msg[1:]
    except:
        return False 
    

msg = getTextMessage()
print(msg)