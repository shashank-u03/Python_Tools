import phonenumbers
import os
import io
from phonenumbers import timezone,geocoder,carrier

# Take phone number as a string

num=input("Enter your number with +__: ")

phone=phonenumbers.parse(num) # Gives details about phone number like country code and National number
time=timezone.time_zones_for_number(phone) # Gives details about timezone
carr=carrier.name_for_number(phone,"en") # en for english like airtel(SIM card info)
valid=phonenumbers.is_valid_number(phone)
reg=geocoder.description_for_number(phone,"en")

print(valid)
print(phone)
print(time)
print(carr)
print(reg)


