# basic-flask-template

This repository contains structure and examples for a basic Flask app with a front-end. The htmls are rendered using Jinja, Flask's default template engine.

However, if you wish to have an app with only the back-end, please remove the templates and statics folders and their relavent references (i.e. `render_template()`). Use only `Response` type returns.

## Setup - Local
```bash
conda create -n <env-name> python=3.9 pip
pip install -r requirements.txt
```

## Setup - Heroku
### 1. Creating new app in Heroku
If you are newly deploying a Flask app using Heroku, make sure
1. You have a Heroku account
2. You have a `Procfile` in the repository
3. You have `gunicorn` in your requirements.txt
4. Have Heroku CLI installed

In the terminal, type
```bash
heroku login
```
Complete the signin with the browser when prompted. Use following commands to create a new Heroku app with your repository

```bash
heroku create <appname>
heroku git:remote -a <appname>
```
Goto section 3 and follow the steps
### 2. Clone an existing repository
If you already have an app using a repository, use Git to clone basic-flask-template's source code to your local machine.
Note: Make sure that you are signed into the correct Heroku account in the Heroku CLI.
```bash
heroku git:clone -a <appname>
cd basic-flask-template
```

### 3. Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

```bash
git add .
git commit -m <commit-message>
git push heroku master
```
