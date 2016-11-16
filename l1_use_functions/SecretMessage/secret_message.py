import os
import re
import random

img_path = "/Users/Azumka/workspace/udacity/CPFPython/l1_use_functions/SecretMessage/message"
curr_path = os.getcwd()

def decode_message():
    os.chdir(img_path)
    for file_name in os.listdir(img_path):
        os.rename(file_name, re.sub('[\d]', '', file_name))
    os.chdir(curr_path)

def code_message():
    os.chdir(img_path)
    for file_name in os.listdir(img_path):
        if ".jpg" in file_name:
            os.rename(file_name, str(random.randint(0, 10000)) + file_name)
    os.chdir(curr_path)

decode_message()
#code_message()

   
