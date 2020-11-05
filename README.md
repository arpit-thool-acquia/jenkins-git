## Autonomous Car Mapping
This is a Flask-MongoDB application for an autonomous car mapping through a specified area. It computes the Total Distance Travelled, Total Time taken and Total Refuels required by the car during the task. The user can also view previous travel history.

### Run following instructions

###### Installations 
```
python3 --version (check python installation)
sudo pip3 install virtualenv
virtualenv --version
```
###### MongoDB setup
```
To install MongoDB - Refer https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
```
###### Create VirtualEnv 
```
mkdir project
cd project
virtualenv map_flask
cd map_flask (this folder is uploaded on the repo)
```
###### Install Flask and PyMongo and Activate Environment 
```
source bin/activate
pip3 install Flask pymongo
```
###### Running application 
```
flask run
http://localhost:5000
```
