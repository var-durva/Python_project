import pywhatkit as kit
import datetime

# Current time
now = datetime.datetime.now()

# Target phone number
phone_number = "+918802279834"

# Message to send
message = (
    "Happy New Year!\n"
    "Wishing you a year full of joy, "
    "health, and success!"
)

# Calculate the time for scheduling the message
send_hour = now.hour
send_minute = now.minute + 1  # Send one minute from now

# Handle edge case where minute + 1 goes beyond 59
if send_minute >= 60:
    send_minute -= 60
    send_hour = (send_hour + 1) % 24  # Ensure hour wraps around correctly

# Scheduling the message
kit.sendwhatmsg(phone_number, message, send_hour, send_minute)

print("Message scheduled successfully!")
