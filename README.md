# sustainability-data-analysis
Thanks to [HaywardMorihara](https://github.com/HaywardMorihara) for help getting started!

## Goal:
Learn the skills necessary for a role that requires sourcing and/or analysis of data for making decisions. With a particular interest in environmental/energy data.

Desired Skills:
- Coding basics (variables, types, control-flow, prints, functions, classes, libraries)
- Database analysis/maintenance
- Automation of dataset analysis
- Web scraping
- Visualizing data
- Clean code


## To Do/Learn:
- Basic Python/coding tutorials
  - https://pythonbasics.org/ was my favorite, but https://www.learnpython.org/ or https://www.w3schools.com/python/ might be good
  - Essential Exercises:
    - https://pythonbasics.org/variables/
    - https://pythonbasics.org/strings/
    - https://pythonbasics.org/keyboard-input/
    - https://pythonbasics.org/if-statements/
    - https://pythonbasics.org/for-loops/
    - https://pythonbasics.org/while-loop/
    - https://pythonbasics.org/functions/
    - https://pythonbasics.org/list/
    - https://pythonbasics.org/list-operations/
    - https://pythonbasics.org/dictionary/
    - https://pythonbasics.org/read-file/
    - https://pythonbasics.org/scope/
  - [Nathaniel's Exercise](#nathaniels-exercise) (see below)
  - Importing Libraries (TO FIND)
  - [Object-Oriented Programming](https://pythonbasics.org/#OOP)
- Communicating with a database
  - Try https://towardsdatascience.com/python-and-postgresql-how-to-access-a-postgresql-database-like-a-data-scientist-b5a9c5a0ea43
- Data analysis exercise
- Find interesting data
- Find interesting datasets
- Making HTTP requests
- Web scraping
- Populating database with data from the internet

### Nathaniel's Exercise:
Reading from the data held in the [data.csv](data.csv), output the oldest building in the dataset.

_Tip: You will most likely want to use Python's `split()` function where:_
```python
x="hello,world"
x.split(",")
```
_will output a list with two strings:_

`['hello', 'world']`

Bonus: Output the 3 oldest buildings


## Notes:
### How To...
#### Pull the latest code for this repo from Github (should probably do this everytime)
Open the `Terminal` app (or from VS Code) and do `git pull origin master` (I know it can be more complicated than that so probably should understand this better...)

#### Open VS Code (IDE for writing code):
Open the `Code - OSS (headmelted)` app

#### Open the Python terminal:
Open the `Terminal` app (or from VS Code) and type `python` and press Enter.

Exit it with `exit()`.

To run a Python script, do `python <SCRIPT_FILE>` (make sure terminal is in the correct directory, most likely will need to `cd development/sustainability-data-analysis` first)

#### Open PostgreSQL terminal:
Open the `Terminal` app (or from VS Code) and type `psql` and press Enter. 

#### Push code to Github:
Open the `Terminal` app (or from VS Code) and do:
- `git add .`
- `git commit -m "<DESCRIPTION_OF_CHANGES>"`
- `git push origin master`
(^ understand what this all means later...)


## Installation:
Steps taken to install Python, PostgreSQL on [my Lenovo C330 Chromebook](https://www.lenovo.com/us/en/laptops/lenovo/student-chromebooks/Lenovo-Chromebook-C330/p/88LGCC31078)

Documenting in case I need to reference how I set up things in the future, or in case it helps anybody else.

### Installing Linux
Followed [these steps](https://support.google.com/chromebook/answer/9145439?hl=en)

### Installing Git
Git was already installed upon starting up the Linux terminal. Just needed to [configure my Github account](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) and start this repo.

Saving credentials so I don't need to enter them on every push:
1.  `git config credential.helper store`

### Installing my IDE (VS Code)
I think because my computer has an ARM64 processor, most installations of VSCode weren't working. But found [this](https://github.com/headmelted/codebuilds/releases/tag/30-Mar-20) which seems pretty good.

### Installing Python & `pip`
[Reference](https://docs.python-guide.org/starting/install3/linux/)
1. `sudo apt-get update`
2. `sudo apt-get install python`
3. `sudo ap install python-pip` <- For installing packages, [reference](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)

### Installing PostgreSQL
1. `sudo apt install postgresql`
2. Great directions for setting up a user PostgreSQL database for local development [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
