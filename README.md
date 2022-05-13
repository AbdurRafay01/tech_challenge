# OWID-COVID Dataset REST API

This repository contains the code for the OWID-COVID Dataset REST API build using the Flask Restful framework.

The APi provides CRUD operations for the dataset which allow the client to interact with the Dataset and perform the operations.

## Getting started

For installing the required libraries such as Flask Restful, requests, etc:
```sh
$ pip install -r requirements.txt
```
Next, clone the repo:
```sh
$ git clone https://github.com/AbdurRafay01/tech_challenge.git
```
## Starting the Flask Server
Start the Flask server:
```sh
$ flask run
```
## Endpoints
The endpoints of the API are:
Endpoint | Description
------- | -------------------------------------------------------------------------------------------------------------------------- 
http://127.0.0.1:5000/covid_data/<int:id> | For GET, PATCH & DELETE requests
http://127.0.0.1:5000/covid_data_update | For PUT requests
http://127.0.0.1:5000/covid_data/auth | For POST requests
## Requests
Method  | Description                                                                                                               
------- | -------------------------------------------------------------------------------------------------------------------------- 
GET     | Returns the row of the dataset provided that it's id is given in URI param                                                                                  
PUT     | Inserts a new data row to the dataset, a payload is required which is a list of entries that are to be inserted.                                                            
DELETE  | Deletes the row in the Dataset provided that it's id is given in URI param                                                                                                            
POST    | Returns an authentication token for the API provided that user credentials are given                                                   
PATCH   | Apply a upgrade to a row of the Dataset where id of that row is given with a JSON payload which has columns mapped to their new values                                                                                    
