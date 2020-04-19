# sustainability-data-analysis

## Goal:
Learn the skills necessary for a role where which requires sourcing and/or analysis of data for making decisions. With a particular interest in environmental/energy data.

Desired Skills:
- Coding basics (variables, types, control-flow, prints, functions, classes, libraries
- Database analysis/maintenance
- Automation of dataset analysis
- Web scraping
- Visualizing data
- Clean code


## To Do/Learn:
- Basic Python/coding tutorials
- Communicating with a database
    - https://towardsdatascience.com/python-and-postgresql-how-to-access-a-postgresql-database-like-a-data-scientist-b5a9c5a0ea43
- Data analysis exercise
- Find interesting data
- Find interesting datasets
- Making HTTP requests
- Web scraping
- Populating database with data from the internet


## Notes:
### How To...
#### Open VS Code (IDE for writing code):
Open the `Code - OSS (headmelted)` app

#### Open the Python terminal:
Open the `Terminal` app (or from VS Code) and type `python` and press Enter.

Exit it with `exit()`.

To run a Python script, do `python <SCRIPT_FILE>` (make sure terminal is in the correct directory, most likely will need to `cd development/sustainability-data-analysis` first)

#### Open PostgreSQL terminal:
Open the `Terminal` app (or from VS Code) and type `psql` and press Enter. 

#### Push code to Github:
Open the `Terminal app (or from VS Code) and do:
- `git add .`
- `git commit -m "<DESCRIPTION_OF_CHANGES>"`
- `git push origin master`
(^ understand what this all means later...)


## Installation:
Steps taken to install Python, PostgreSQL on [my Lenovo C330 Chromebook](https://www.lenovo.com/us/en/laptops/lenovo/student-chromebooks/Lenovo-Chromebook-C330/p/88LGCC31078)

Documenting in case I need to reference how I set up things in the future, or in case it helps anybody else.

Thanks to [HaywardMorihara](https://github.com/HaywardMorihara) for help getting started!

### Installing Linux
Following [these steps](https://support.google.com/chromebook/answer/9145439?hl=en)

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