
## How to run this project

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

python3 -m pip install virtualenv

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

