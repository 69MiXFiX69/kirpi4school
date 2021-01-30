import random
import string


print("1) Easy pass\n"
      "2) Middle level pass\n"
      "3) Strong-ass pass")
passtype = int(input('Please select your password type \n'))
password = ''

if passtype == 1:
    for x in range(8):
        password = password + random.choice(string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits)
    print(password)
elif passtype == 2:
    for x in range(16):
        password = password + random.choice(string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits)
    print(password)
elif passtype == 3:
    for x in range(32):
        password = password + random.choice(string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits)
    print(password)
else:
    print("Wrong password type")