# Featkeeper

[![Build Status](https://travis-ci.org/ivansabik/featkeeper.svg)](https://travis-ci.org/ivansabik/featkeeper)

Featkeeper is a web app for creating and tracking feature requests from clients for different products

## Tools

- Flask
- MongoDb
- PyMongo
- Boostrap
- Pandas

## Use cases

![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/use_cases.png)

## Agent user stories (specs)

- As an agent I should be able to create a new feature requests
- As an agent I should be able to view feature requests created by me
- As an agent I should be able to edit a feature requests
- As an agent I should be able to close a new feature request

## Models

![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/models.png)

## API endpoints

- /api/v1/feature-request
- /api/v1/agent
- /api/v1/client

### Example for FeatureRequest

### Example for Agent

### Example for Client

## Routes in client app

## Views in client app

Login

![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/login.png)

Dashboard

![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/dashboard.png)

New feature request

![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/new_feature.png)

Edit feature request

![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/edit_feature.png)

## Working example

A working sample app can be fount at:
http://

## Deploy

```
$ git clone http://git.enable.mx/ivansabik/featkeeper.git
$ cd featkeeper
$ virtualenv venv
$ . venv/bin/activate
(venv)$  pip install -r requirements.txt
(venv)$ python api.py
```

## Run tests

```
$ python -m unittest discover
```
