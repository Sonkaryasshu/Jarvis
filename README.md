# Jarvis

Jarvis is a smart personal voice assistant which can be used to send emails, search wikipedia, browse youtube, open any application etc.
In this project we are going to use python with some of freely available  libraries.

## Requirements:
Following python packages are required:
- pyttsx3
- speech_recognition
- wikipedia
- webbrowser
- smtplib
- datetime
- os

***Note -*** If you dont't have any of this package not installed on your system, you can easily install that package by running command `pip install <package-name>` or `pip3 install <package-name>`.
ex: `pip3 install wikipedia`
#### Additional requirements:
To send  email from this program you need a mail-id of `gmail.com` domain and you have to enable less secured applications on your google account.

You also need to add your email-id and password under `sendEmail` function and the receiver's email-id at the `main` section of our program under the `email to <reciever-name>` section.

## Steps to run it on your system:

**Note:** I am using python-3.6.8

1. Get this project to your local system
	> git clone https://github.com/Sonkaryasshu/Jarvis.git

2. Change directory to current project
	>cd jarvis
	
3. Run the python file

	> python main.py


### Working
After executing `python main.py` command, you will be greeted by our application and then waits for your command. You can give voice command like `jarvis open notepad`, `jarvis send email to kuldeep`, `jarvis what's the time now`, etc.

- To exit from the program simply say `jarvis shutdown` and program will be closed. 


