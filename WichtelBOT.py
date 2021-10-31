# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 16:10:11 2021

@author: oo_emperor
"""

import random
import smtplib
import copy

"""
config file is the mail settings in form:
mail adress;password;smtp server;
"""

f = open("config.txt")
file = f.read()
f.close()
config = file.split(";")

MAIL_ADRESS = config[0]
PASSWORD = config[1]
SMTP_SERVER = config[2]

def sendMail(receiver, subject, msg):
    #Send a Mail to the receiver with message msg and subject
    #context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, 587) as server:
        server.login(MAIL_ADRESS, PASSWORD)
        message_text = ("From: " + MAIL_ADRESS + "\n" + "To: " + receiver + "\n" + "Subject: " + subject + "\n\n" + msg)
        server.sendmail(MAIL_ADRESS, receiver, message_text)

def wichteln_list_generator():
    #members is a list of all participants
    #creates a second list with who is wichtel for who
    members = [] #You need to put Members in here
    members2 = copy.deepcopy(members)
    list_wichtel = []
    
    for i in range(len(members)):
        rand = random.randint(0, len(members2)-1)
        list_wichtel.append(members2[rand])
        members2.pop(rand)
    return (members, list_wichtel)


def check_lists_wichtel(list1, list2):
    #Compares two lists if two elements at the same position are identical
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                return(1)
                break
            else:
                continue
        return(0)
    else:
        return(404)


def wichteln():
    #Function to check if no one will have himself for the Wichteln
    while True:
        (list1, list2) = wichteln_list_generator()
        if check_lists_wichtel(list1, list2) == 0:
            print(list1)
            print(list2)
            for i in range(0, len(list1)):
                sendMail(get_mail_from_name(list1[i]), "betreff", "message)
            break
        else:
            continue
        
        
def get_mail_from_name(name):
    #Takes name in form of Surname Name as input
    list_name = name.split(" ")
    mail = str(list_name[0]) + "." + str(list_name[1]) + "@" #replace with your domain id
    return (mail)
     

#Starts all the needed functions

#wichteln()
#sendMail("mail", "theme", "message")
wichteln()
print(get_mail_from_name("5 6"))
