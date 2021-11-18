# Python Project Boilerplate

Simple boilerplate for starting a python proect.

# Using the repo

Follow following steps to install client on server

1. Create a virtual environment.
Copy-paste following code to create one.
```
python -m venv env
```
or for linux:
```
python3 -m venv env
```

2. Activate the virtual environment.
```
env\Scripts\activate
```
or for linux:
```
source env/bin/activate
```

3. Install the required pacakages from requirements.txt file.
```
pip install -r requirements.txt
```

4. Install the pre-commit hook for formatting code.
This installs the pre-commit hook to your local git project.
```
pre-commit install
```

5. Configure the pre-commit parameters.
Configure the `.pre-commit-config.yaml` according to your requirements. Before these changes are reflected, you need to stage the file by:
```
git add .pre-commit-config.yaml
```
The code is formatted whenever you commit your changes but this does not stage your changes.

6. Run the pre-commit command before staging your changes.
```
pre-commit run
```

7. Run the project.
```
python main.py
```
