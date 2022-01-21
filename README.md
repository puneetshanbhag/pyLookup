
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

**The rule of thumb here is to have the same lookup keys/field in both the excel.**

under ``` ┣ 📂input``` folder we have to keep this files, name it appropriately and the same file names to be used in the code as well.

```
workbook_one = 'input/input1.xlsx'
workbook_two = 'input/input2.xlsx'
```

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


### Step 3:

After all the above steps are done, we need to run the ```pyLookup.py``` file and the result will be dumped under ``` ┣ 📂output ``` folder.

The output file naming convention is as below:

``` lookup_output_<timestamp>.xlsx ```

example :
``` lookup_output_1642776880.xlsx ```

