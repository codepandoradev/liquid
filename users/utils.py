import hashlib
import time

def generate_token():
    return hashlib.md5(str(time.time()).encode()).hexdigest().upper()*3


def encode_password(password:str): 
    return hashlib.md5(password.encode()).hexdigest()
    

def email_to_nick(email:str):
    output = ""
    for char in email:
        if char!="@": output+=char
        else: break
        
    return output

print(email_to_nick("sdsadas@mail.com"))