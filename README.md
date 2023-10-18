
# OKKGG Website 
<p align="left"> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

# Start the web server
## How to first run this project

### Install Python

- Install the lastest python version : https://www.python.org/downloads/

### Install pip

```bash
python3 -m pip install
```
then check the version to be sure the installation was correctly done: 
```bash
python3 -m pip --version
```

### Install virtualven
```bash
python3 -m pip install virtualenv
```
### Optional step: Use git to clone and update the project!
```bash
git clone https://github.com/Cafe-Soluble/okkgg.git
git remote add origin https://github.com/Cafe-Soluble/okkgg.git
```


### Go to the project folder

```bash
  cd Path/To/The/Project/Folder/
```
You can verify if you are in the project folder by using both command lines: 
```bash
  pwd
```
or
```bash
  ls
```

### Create a new virtual environment (MacOS and Linux)

```bash
  python3 -m venv env
```

### Activate the new environment (MacOS and Linux)

```bash
source env/bin/activate
```
### Install the requirements
```bash
pip install -r requirements.txt
```

### Start the python server 

```bash
    python3 main.py
```

And open your webrowser to http://localhost:5000/

## How to run this project when all the requirements are already installed

### Go to the project folder

```bash
cd Path/To/The/Project/Folder/
```

Better option : just open the folder in VS Code and use the terminal inside the software ; you'll be in the main folder project.

### Optional step: update the last version of this project with Git: 
You need to have followed the Git instructions for the previous installation procedure, then : 
```bash
cd git pull origin main
```
### Run the following command lines: 

```bash
source env/bin/activate
```
```bash
python3 main.py
```

And open your webrowser to http://localhost:5000/

# How does the server and website work?
## File structure
Html files are always in the <b>templates</b> folder.
Images, videos and music files are always in the <b>static</b> folder.


## Links to other pages
Links to other pages don't work the same way as with "classic" HTML. You need to use <b>url_for("")</b>. Just look at some example inside the <b>index.html</b>.  


## The layout
The <b>layout.html</b> file contains all the information present on all pages of the website (navbar, footer, etc.).