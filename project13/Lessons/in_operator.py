#!/usr/bin/python3 

my_answer = input("What is your answer ? ")

options = ["rock", "paper", "scissors"]

#if my_answer in options:
#    print("Rock is one of the possible options!")
#else:
#    print("Wrong answer try again ")


key = "name"
person = {
    "name": "Kalob",
    "profession": "Coding teacher",
}

if key in person:
    print ("Name is a valid dictionary key in the person object")

opt_set= set(options)

if 'paper' in opt_set:
    print("Found ")