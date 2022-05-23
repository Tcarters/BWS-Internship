#!/usr/bin/python3


from tkinter.filedialog import Open


with open('emails.txt', 'r') as emails:
    emails = emails.readlines()

for email in emails:
    if "gmail" in email:
        print(email.rstrip())