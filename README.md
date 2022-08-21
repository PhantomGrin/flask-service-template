# basic-flask-template
### Setup - Local
```bash
conda create -n <env-name> python=3.9 pip
pip install -r requirements.txt
```

### Creating new app in Heroku

`heroku login`

Complete the signin with the browser when prompted. Use following commands to create a new Heroku app with your repository

```bash
heroku create <appname>
heroku git:remote -a <appname>
```

### Clone the repository
If you already have an app using a repository, use Git to clone basic-flask-template's source code to your local machine.
```bash
heroku git:clone -a basic-flask-template
cd basic-flask-template
```
### Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

```bash
git add .
git commit -m <commit-message>
git push heroku master
```
