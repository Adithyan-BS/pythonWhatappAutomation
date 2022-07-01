import pywhatkit

try:
    phoneNumber = input("Enter phone number")
    pywhatkit.sendwhatmsg(phoneNumber,"Test whatsapp",16,29,5,True)

    print("Message Sent!")

except:
    print("Error in sending the message")