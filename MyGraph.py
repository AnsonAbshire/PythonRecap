import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")

#Virtual Environment Notes
#you have to install a library, create a virutal environemnt (python copy), copy library into it - to get certain modules
#1. create a VE (virtual envrionement) in terminal - py for PC, python3 for MAC; code: "py -3 -m venv (name)"; "venv" is the command; "myvenv" is the name of the VE
#2. activate your VE - copies python interpreter to your folder - type in location of activate file for PC "(name)\Scripts\activate" 
#3. Install 3rd party library/module - "pip3 install (library name)"

#Git Configuration
#git config --global user.name "Anson"
#git config --global user.email "Anson_Abshire1@baylor.edu"