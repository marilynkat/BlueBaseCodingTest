# API Instructions
This repo consists if 5 different APIs. They all have the same functionality but each one deals with a different dataset. \
Each API is titled dataset# where the # can be replaced with a number from 1-5. \
Each number corresponds to the following dataset:
1. https://bluebase.blob.core.windows.net/internship/df_1.csv
2. https://bluebase.blob.core.windows.net/internship/df_3.csv
3. https://bluebase.blob.core.windows.net/internship/df_4.csv
4. https://bluebase.blob.core.windows.net/internship/df_5.csv
5. https://bluebase.blob.core.windows.net/internship/df_6.csv

## Endpoint and Functionality
### /dataset#/
- GET: Returns all of the entries in the database
- POST: Allows user to submit entry into database

### /dataset#/[id] 
- GET: Returns data about 1 database entry
- PUT: Edit data about 1 database entry
- DELETE: Deletes 1 database entry

### /dataset#/populate
- GET: Clears database and populates from csv file
