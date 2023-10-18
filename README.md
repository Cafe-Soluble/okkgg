
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
### Optional : Use git to clone and update the project !
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

### Optional : update the last version of this project with Git : 
You need to have followed the Git instructions for the previous installation procedure, then : 
```bash
  cd git pull origin main
```
### Run the following command lines : 

```bash
source env/bin/activate
```
```bash
    python3 main.py
```

And open your webrowser to http://localhost:5000/

# How does the server and website work?
## File structure
Html files are always in the templates folder
Images, videos, music files, etc. are always in the static folder.


## Links to other pages
Links to other pages don't work the same way as with "classic" HTML. You need to use url_for(""). Just look at some example inside the index.html.  


## The layout
The layout.html file contains all the information present on all pages of the website (navbar, footer, etc.).