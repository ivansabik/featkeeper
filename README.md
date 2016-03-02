# Featkeeper
[![Build Status](https://travis-ci.org/ivansabik/featkeeper.svg)](https://travis-ci.org/ivansabik/featkeeper)

Featkeeper is a web app for creating and tracking feature requests from clients for different products. It's built using and API on top of Python and MongoDb for data persistence and a client app in JS.

Great props to Miguel Grinberg for his excellent book on Flask and his [tutorial for integrating with KnockoutJs](http://blog.miguelgrinberg.com/post/writing-a-javascript-rest-client)


## Tools
- [flask](https://github.com/mitsuhiko/flask)
- [mongothon](https://github.com/gamechanger/mongothon)
- [shortuuid](https://github.com/stochastic-technologies/shortuuid)
- [knockout.js](https://github.com/knockout/knockout)
- [bootstrap](https://github.com/twbs/bootstrap)
- [atom](https://atom.io/), the best text editor I have ever known, free and open source

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
### /api/v1/feature-request

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

### /api/v1/feature-request/:id

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
A working sample app can be fount at: http://

## Deploy

```shell
$ git clone https://github.com/ivansabik/featkeeper
$ cd featkeeper
$ virtualenv venv
$ . venv/bin/activate
(venv)$  pip install -r requirements.txt
(venv)$ python featkeeper/app.py
```

Now the api is listening at [http://127.0.0.1:5000/api/v1/](http://127.0.0.1:5000/api/v1/)

## Test data
A script is provided for generating test data, can be accessed with:

```shell
$ python featkeeper/setup_dev_data.py
```

## Tests
Functional with Selenium and unit with unittest. Run test suites with:

```shell
$ python -m unittest discover
```
