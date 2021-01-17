## devamigo

![alt text](./Work-Smarter-Not-Harder.png)

# Purpose

When working i find it very common to copy/paste appearing errors to stackoverflow.com. To work smarter and save some time we automize that process saving many minutes of our work daily.

# Requirements

- Python3.x (tested on Python3.7.7)

- pip install -r requirements.txt

# Usage

- python devamigo.py {desired command}

For testing in our project works commands like

- python devamigo.py python ProgramExample/error.py

- python devamigo.py javac ProgramExample/HelloWorld.java

# Current functionality

Our application now captures errors from compiling programs, passed them to analize location of errors, sends request for best answer and for each error provide view in browser to beggining of answers and link to stackoverflow.com

In config.json you can modify:
- number of answers to each error
- number of characters shown in soultions preview
- site to search for answers
- if you want open browser automaticly with solutions preview

# Future plans

- Test application with other programming language
- Build application to work without requirement to install python libraries

## Contributors

- Michał Ćwierz - Team Leader
- Jakub Świerczyński
- Łukasz Szajnoga
- Szymon Flis
