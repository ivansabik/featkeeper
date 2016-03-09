# ![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/logo.png) Featkeeper
[![Build Status](https://travis-ci.org/ivansabik/featkeeper.svg)](https://travis-ci.org/ivansabik/featkeeper) [![Coverage Status](https://coveralls.io/repos/github/ivansabik/featkeeper/badge.svg?branch=master)](https://coveralls.io/github/ivansabik/featkeeper?branch=master)

Icon made by [freepik](http://www.flaticon.com/free-icon/cat-face-outline_57104) from www.flaticon.com

![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/demo.gif)

Featkeeper is a web app for creating and tracking feature requests from clients for different products. It consists of two core components:
- API on top of Python and MongoDb for data persistence
- Client app in JS

Client app and server app are independent components! (Flask / KnockoutJS)

Great props to Miguel Grinberg for his excellent book on Flask and his [tutorial for integrating REST APIs with KnockoutJS](http://blog.miguelgrinberg.com/post/writing-a-javascript-rest-client)

## Tools
### API (Python)
- [flask](https://github.com/mitsuhiko/flask)
- [mongothon](https://github.com/gamechanger/mongothon)
- [shortuuid](https://github.com/stochastic-technologies/shortuuid)
- [Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth)

### Client app (Javascript)
- [knockout](https://github.com/knockout/knockout)
- [bootstrap](https://github.com/twbs/bootstrap)
- [bootstrap-datepicker](https://github.com/eternicode/bootstrap-datepicker)
- [jquery](https://github.com/jquery/jquery)
- [moment](https://github.com/moment/moment)

## Use cases
![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/admin_use_cases.png)

![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/agent_use_cases.png)

## Admin user stories (specs)
- As an admin I should be able to login (do auth)
- As an admin I should be able to create a new user
- As an admin I should be able to view current users
- As an admin I should be able to edit a user
- As an admin I should be able to disable access for a user

## Agent user stories (specs)
- As an agent I should be able to login (do auth)
- As an agent I should be able to create a new feature requests
- As an agent I should be able to view feature requests
- As an agent I should be able to edit a feature request
- As an agent I should be able to close a new feature request

## Models
![](https://raw.githubusercontent.com/ivansabik/featkeeper/master/doc/models.png)

## API endpoints
Delete actions do not exist, instead an attribute/field is used to check models' current status which can be updated using PUT requests. This allows to recover objects as opposed to deleting the API resources. This also allows better logging and analytics.

### GET /api/v1/feature-request

```javascript
{
  "feature_requests": [
    {
      "_id": "56d3d524402e5f1cfc273340",
      "agent_name": "Eleuthere",
      "client_name": "Mandel Jamesdottir",
      "client_priority": 1,
      "created_at": "2016-02-28 23:35:19",
      "description": "Client wants to be able to choose different colors, fonts, and layouts for each module",
      "is_open": 1,
      "product_area": "Policies",
      "target_date": "2016-08-21",
      "ticket_url": "http://localhost:5000/LhPnCk",
      "title": "Support custom themes"
    },
    {
      "_id": "56d3d524402e5f1cfc273344",
      "title": "Support Google account auth",
      "description": "Client wants to be able to login using Google accounts restricted to users in corporate domain",
      "client_name": "Carlo Fibonacci",
      "client_priority": 2,
      "target_date": "2016-06-15",
      "ticket_url": "http://localhost:5000/8VZuWu",
      "product_area": "Billing",
      "agent_name": "Eleonor",
      "created_at": "2015-12-20 09:15:20",
      "is_open": 1
    }
  ]
}
```

### GET /api/v1/feature-request/:id

```javascript
{
  "_id": "56d3d524402e5f1cfc273340",
  "agent_name": "Eleuthere",
  "client_name": "Mandel Jamesdottir",
  "client_priority": 1,
  "created_at": "2016-02-28 23:35:19",
  "description": "Client wants to be able to choose different colors, fonts, and layouts for each module",
  "is_open": 1,
  "product_area": "Policies",
  "target_date": "2016-08-21",
  "ticket_url": "http://localhost:5000/LhPnCk",
  "title": "Support custom themes"
}
```

### POST /api/v1/feature-request/
 HTTP request with body:

```
{
    "title": "Add end to end encripted chat",
    "description": "Client wants to be able to send P2P encrypted messages to customers in realtime",
    "client_name": "Akbar Erickssohn",
    "client_priority": 1,
    "target_date": "2016-10-29",
    "product_area": "Policies",
    "agent_name": "Eleuthere"
}
```

Will return something like:

```javascript
{
  "feature_request": {
    "_id": "56dcd6cf402e5f3fd6b9b360",
    "agent_name": "Eleuthere",
    "client_name": "Akbar Erickssohn",
    "client_priority": 1,
    "created_at": "2016-03-06 19:18:07",
    "description": "Client wants to be able to send P2P encrypted messages to customers in realtime",
    "is_open": 1,
    "product_area": "Policies",
    "target_date": "2016-10-29",
    "ticket_url": "http://localhost:5000/er78Bg",
    "title": "Add end to end encripted chat"
  },
  "message": "Feature request added",
  "status": "success"
}
```

### PUT /api/v1/feature-request/:id
Given that a feature request with ID 56dcc6bf402e5f329f71bde9 exists, HTTP request with body:

```
{
  "_id": "56dcc6bf402e5f329f71bde9",
  "is_open": 0
}
```

Will return something like:

```javascript
{
  "feature_request": {
    "_id": "56dcc6bf402e5f329f71bde9",
    "agent_name": "Eleuthere",
    "client_name": "A",
    "client_priority": 5,
    "created_at": "2016-03-06 18:09:35",
    "description": "Client wants to be able to choose different colors, fonts, and layouts for each module",
    "is_open": 0,
    "modified_at": "2016-03-06 18:44:54",
    "product_area": "Policies",
    "target_date": "2016-08-21",
    "ticket_url": "http://localhost:5000/WKRuRz",
    "title": "Support custom themes"
  },
  "message": "Feature request updated",
  "status": "success"
}
```

## Views in client app
KnockoutJS as other popular frameworks follow a wide known pattern called [Model-view-viewmodel or MVVM](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel). For this, the following HTML views are implemented:
- Feature requests
- New feature request
- Edit feature request

The implemented ViewModels are:
- FeatureRequestViewModel
- NewFeatureRequestViewModel
- EditFeatureRequestViewModel

## Setup a dev environment in Mint/Ubuntu

```shell
$ sudo apt-get update
$ sudo apt-get install git python python-pip python-all-dev mongodb nodejs python-virtualenv
$ sudo apt-get install npm
$ npm install -g grunt-cli
$ git clone https://github.com/ivansabik/featkeeper
$ cd featkeeper
$ npm install
$ grunt
$ virtualenv venv
$ . venv/bin/activate
(venv)$  pip install -r requirements.txt
(venv)$ python featkeeper/app.py
```

Now the API is listening at: [http://127.0.0.1:5000/api/v1/](http://127.0.0.1:5000/api/v1/)

For development, the client app can be statically served from: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Run
Run using test db:

```shell
$ python featkeeper/app.py --mode test
```

Run listening in public IP:

```shell
$ python featkeeper/app.py --public true
```

## Test data
A script is provided for generating test data, can be accessed with:

```shell
$ python featkeeper/setup_dev_data.py
```

## Run functional and unit tests
Functional tests with Selenium and unit tests with unittest:

```shell
$ nohup python featkeeper/app.py --mode test &
$ python -m unittest discover
```

After running tests you can kill the Flask process:

```shell
fuser 5000/tcp
```
