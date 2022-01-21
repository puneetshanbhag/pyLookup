
# Pylookups - A simple lookup tool

This is a small script used to perform lookups (similar like vlookup in excel), 
The main purpose of this script is to automat the predefined lookup process.

## Steps to compile the code in a virtual environment

### Step 1: (Windows only)
- Create python virtual environment 

    ``` py -3 -m venv .venv ```

- Activate the virtual environment

    ``` .venv\scripts\activate ```

- Install all the dependency using below command

    ``` pip install -r .\requirements.txt ```

After following above step 1 , you should see a folder
```📂.venv``` with all the dependency of the project installed under it.


### Step 2:

This piece of code required us to provide 2 input files, the first input file is the file from where we need to perform the lookup based on the lookup key, and the second file is the one from where we need to fetch values for a given key in the first sheet.

**So the rule of thumb here is to have the same lookup keys/field in both the excel.**




The project have following folder structure

```📦pyLookup
 ┣ 📂.venv
 ┣ 📂input
 ┃ ┣ 📜input1.xlsx
 ┃ ┗ 📜input2.xlsx
 ┣ 📂output
 ┣ 📜pyLookup.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```

```📂.venv``` 