# Full Stack Casting Agency API Backend

## Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Motivation for project

This is the capstone project of Udacity fullstack nanodegree program, which allows demonstrating multiple skills including SQLAlchemy (ORM), Postgres,  Flask, Auth0, Gunicorn and Heroku to develop and deploy a RESTful API.

## Getting Started

### Installing Dependencies

#### Python 3.7.9
[Python Instllation](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup please install dependencies:

```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM that is utilized to handle the lightweight sqlite database. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python app.py
```

#### Flask run tests the token headers set for the enviroment. If they have expired, you need to login using the crededntials below and replace them in setup.sh and run setup.sh again

.env has all the environment variables needed for the project. The app may fail if they are not set properly.

# Project deployed at

https://cj-fsnd-capstone-castingagency.herokuapp.com/

###### To test live APIs the only way right now to do this is curl requests. Add Auth token headers from logins below to test.

OATH login url. There are three logins atm, JWTs for these appear in the url after successfull login. Those tokens are needed to test the different APIs.


https://testauth-cj.us.auth0.com/authorize?audience=fsnd-capstone&response_type=token&client_id=Z8egxrrct2565gBOusHiBznFh1rg9Ui1&redirect_uri=https://127.0.0.1:8080/login-results

Casting Assistant (castingagent@fsnd.com - pass - Test!123)

Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVOX3hfRldDczV2N295WHB3MXhCUiJ9.eyJpc3MiOiJodHRwczovL3Rlc3RhdXRoLWNqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmM0NjNjZjhhMDZjNTc2YjM3MWYyZTQiLCJhdWQiOiJmc25kLWNhcHN0b25lIiwiaWF0IjoxNjU3MDQ3MDYxLCJleHAiOjE2NTcxMzM0NjEsImF6cCI6Ilo4ZWd4cnJjdDI1NjVnQk91c0hpQnpuRmgxcmc5VWkxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.ZcetdG3QcNWnEmAP-vFa9GlS__fvFEKvXrJCMvw1d-yaoDIJ6ATVOn2UGUULs02NvlAeq2EiDs-r7cVG7wLrdnHF1MjmeV8ROyaYI1fV_cFfXySMHRC0vJ12Y3qamT9YHHOnP9vjh7-MeiQhCr1soF_ktKPlt6M-_OV_ks_RAyMsBR-NIEuAlnEYr0WJILMVrN5ZtN2aO5WqAxAjjn_tIjjKPJS--XR9xvueKDZydf2GRZ3lms-eUt4cHEuP01fhZe7lqFoUsJs862zYe18rLsCupsZQjeQz8KVFu1gI5MoNCfNCNdzIjglBtY5H_aQoElXnTzAGJA3hQ-6bVkdR_A
```

Casting director  (director@fsnd.com - pass - Test!123)

Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVOX3hfRldDczV2N295WHB3MXhCUiJ9.eyJpc3MiOiJodHRwczovL3Rlc3RhdXRoLWNqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmM0NjQ3NThhMDZjNTc2YjM3MWYzMDAiLCJhdWQiOiJmc25kLWNhcHN0b25lIiwiaWF0IjoxNjU3MDQ3MDk5LCJleHAiOjE2NTcxMzM0OTksImF6cCI6Ilo4ZWd4cnJjdDI1NjVnQk91c0hpQnpuRmgxcmc5VWkxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.g3pJGROCLtKTJ7d4_kQZCPLVXQeZSru-5YOc90nMrs2A-WfhUohenmPpB4gwL5GhrN5VAqEvGRBF7tj8TmtCJvSPlNgiw6F57Y8hzW8-md2LoKakUluEd0U0SnICW5eDIi25gcOcZvVmB9dBAjoTHQIvG4ybCyfBEQ1i78RzsadrO2Xy-biMLUuq4ks6S7RWQs7pFp8OUC0ChvRQI1Yh0-Y4IIAoRVBaVp9TpsRZ9zYJHMG_jLyddsduyPQY3t8NZ39eEH_3QCYBLzxKhkkPWaUfmGTHtm0kFedAFi3n2BK-K8N2rizTFVPNw6DGcLFTx0rdMyepT_7e18YDnrA4Ow
```

Executive Producer (producer@fsnd.com - pass - Test!123)

Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVOX3hfRldDczV2N295WHB3MXhCUiJ9.eyJpc3MiOiJodHRwczovL3Rlc3RhdXRoLWNqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmM0NjRkNDhhMDZjNTc2YjM3MWYzMjYiLCJhdWQiOiJmc25kLWNhcHN0b25lIiwiaWF0IjoxNjU3MDQ2OTM2LCJleHAiOjE2NTcxMzMzMzYsImF6cCI6Ilo4ZWd4cnJjdDI1NjVnQk91c0hpQnpuRmgxcmc5VWkxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.E-jyvZvCq4A5ZfxeQHfX9dQH_q0g-_GG3dTaF6L3XJlrmmi-kepNTH60hgkclyV6x_JaJMsHbbNLF2UZA7PxZvQeLZYs1xsgp92qwVYO4hXeM7cBloIUHIH3vEuIL9jCxFr69m6pBpwcWQhIcQrfVHHGzcj4y3gc2n0Dn6Y8KtIetNJkRVW2A6bvmCCrwqAzVnixFnBi4yT0IokRYLRvBMItXs3AXVXoIOEBX9YYklDc4J-cR1tfq315O3FnpdphzUlrEg8g8xktZmpFyhWk3Qu0gJP1jBz2KGiLnItCKEq1iOOwtvUEXPZ3YZSXyVbS0CqUhQEnYc3T98YXs4RL-Q
```

## Testing

To run the tests locally, run

```
python test_app.py
```

The tests print data returned from the APIs along with API logs.

#### The rests also use the Auth token set in env variables and will give an error if the tokens are expired.

## API Reference

### Endpoints

GET '/actors'
POST '/actors'
PATCH '/actors/<id>'
DELETE '/actors/<id>'
GET '/movies'
POST '/movies'
PATCH '/movies/<id>'
DELETE '/movies/<id>'
----------------------------------------------------------------------------------

GET '/actors'
Gets all the actors present in the database
URL Argument : None
Data Arguments : None
Returns : Json with all the actor ID,name, age and gender 
Sample successful response:

```
{
    "actors": [
        {
            "age": 76,
            "gender": "male",
            "id": 6,
            "name": "Amitabh B"}
        ],
    "success": true    
}
```

POST '/actors'
Create a new actor in the database
URL Argument : None
Data Arguments : age, name, gender
Sample Input :
```
{
    "age":75,
    "name": "Amitabh Bachhan",
    "gender": "male"
}
```
Returns : Json with the ID,name, age and gender 
Sample successful response:
```
{
    "actors": {
        "age": 75,
        "gender": "male",
        "id": 11,
        "name": "Amitabh Bachhan"
    },
    "success": true
}
```

Patch '/actors/<id>'
Update an actor already in the database
URL Argument : Actor id
Data Arguments : age or/and name or/and gender
Sample Input :
```
{
    "gender": "male",
    "name": "Amitabh B",
    "age":76
}
```
Returns : Json with actor ID,name, age and gender 
Sample successful response:
```
{
    "actor": {
        "age": 76,
        "gender": "male",
        "id": 11,
        "name": "Amitabh B"
    },
    "success": true
}
```
Delete '/actors/<id>'
Delete an actor from the database
URL Argument : Actor id
Data Arguments : None
Returns : Json with all the id of the actor which is deleted
Sample successful response:
```
{
    "id": 11,
    "success": true
}
```

GET '/movies'
Gets all the movies present in the database
URL Argument : None
Data Arguments : None
Returns : Json with all the title, id and release date
Sample successful response:

```
{
    "movies": [
        {
            "id": 3,
            "release_date": "2027-11-11",
            "title": "Don"
        } ],
    "success": true
}
```

POST '/movies'
Create a new movie in the database
URL Argument : None
Data Arguments : title, release date
Sample Input :
```
{
    "title": "Don",
    "release_date":"2027-11-11"
}
```
Returns : Json with the ID,name, age and gender 
Sample successful response:
```
{
    "movies": {
        "id": 9,
        "release_date": "2027-11-11",
        "title": "Don"
    },
    "success": true
}
```

Patch '/movies/<id>'
Update a movie already in the database
URL Argument : Movie id
Data Arguments : title and/or release date
Sample Input :
```
{
    "title": "The Terminal",
    "release_date" : "2005-06-01"
}
```
Returns : Json with ID,release date and title
Sample successful response:
```
{
    "movie": {
        "id": 5,
        "release_date": "2005-06-01",
        "title": "The Terminal"
    },
    "success": true
}
```
Delete '/movies/<id>'
Delete a movie from the database
URL Argument : movie id
Data Arguments : None
Returns : Json with id
Sample successful response:
```
{
    "id": 5,
    "success": true
}
```
### Error Handling

Errors are returned as JSON objects. 
Sample format :

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}

```

## Authors

Charanjeet Singh Arneja