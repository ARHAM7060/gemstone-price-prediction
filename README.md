## GEMSTONE PRICE PREDICTION

### STEP1. CREATION OF ENVIRONMENT 
```
COMMAND TO CREATE ENVIRONMENT   - 'conda create -p venv python==3.8'
COMMAND TO ACTIVATE ENVIRONMENT - 'conda activate venv/'
```

### STEP2. CREATION OF REQUIREMENTS.TXT FILE
```
NAME         - requirements.txt
INSTALLATION - pip install -r requirements.txt
```

### STEP3. CREATION OF SETUP.PY FILE
```
NAME            - setup.py
command to run  - python setup.py install
```

### TO TRIGGER SETUP.PY USING REQUIREMENTS.TXT
```
WRITE '-e .' TEXT IN THE REQUIREMENTS.TXT FILE
NOW IF WE RUN REQUIREMENTS.TXT FILE SETUP.PY FILE WILL ALSO RUN
```

### MAKING THE PROJECT STRUCTURE
```
notebooks folder
   -
src folder
   -components folder
      -__init__.py
      -datai_ngestion.py
      -data_transformation.py
      -model_traner.py
   -pipeline folder
      -__init__.py
      -prediction_pipeline.py
      -training_pipeline.py
   -__init__.py
   -exception.py
   -logger.py
   -utils.py
venv folder
.gitignore
README.md
requirements.txt
setup.py


```

### CREATE EDA.ipynb FILE IN notebooks FOLDER
```
TO RUN STATEMENTS IN THIS FILE WE NEED TO INSTALL IPYKERNEL

```

### EDA 
```
STEP1.  IMPORT DATASET
STEP2.  CHECK FOR NULL VALUES
STEP3.  CHECK FOR CATEGORICAL VARIABLES
STEP4.  DROP UNWANTED COLUMNS
STEP5.  SEGREGATING NUMERICAL AND CATEGORICAL COLUMNS
STEP6.  FINDING UNIQUE VALUES AND FREQUENCIES OF VALUES OF CATEGORICAL COLUMNS
STEP7.  CREATING PLOTS OF EACH FEATURE
STEP8.  CREATING HEATMAP TO SEE THE CORRELATION BETWEEN NUMERICAL FEATURES
STEP9.  CREATING RANKING VALUES DICTIONARY FOR ORDINAL VALUES AND THEN MAPPING IN THE DATASET
```