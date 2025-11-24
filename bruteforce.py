import itertools

test_str = "123456789"

for pw_length in range(1, 5) : 
    for pw in itertools.product(test_str, repeat=pw_length) : #product = for와 동일함
        print(''.join(pw)) 