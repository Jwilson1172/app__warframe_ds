[![Build
Status](https://travis-ci.com/Jwilson1172/warframe_ds.svg?branch=master)](https://travis-ci.com/Jwilson1172/warframe_ds)
<a href="https://heroku.com/deploy" style="display: block"><img src="https://www.herokucdn.com/deploy/button.svg"
        title="Deploy" alt="Deploy"></a>

# Warframe Market Prediction Project ( WMPP )
## A Warframe Market scrapper that takes data from the API for the warframe market and tries to predict the trends of
the market for most of the items that are in the Warframe player market based on a historical trends and external
considerations for the items values(events, accolyte invasions, sorties ect)


## Road Map/ current dev tasks

<div>

    - get a dash app deployed and supporting a user login
    - set up an ETL pipeline to start serving data about the warframe market
    - get a list of warframe market items in a database for lookups
    - provide a predictions graph for items using the model

</div>

# Running locally

Run the following commands to bootstrap your environment if you are unable to run the application using Docker

```bash
cd app__warframe_ds
pip install -r requirements/dev.txt
```

Once you have installed the project dependencies you can run the app locally with the command

```bash
flask run
```
# Deployment

## Heroku

The best effort has been made to make deployment as easy and seamless as possible, however you should
familiarize yourself with the basic [Git](https://git-scm.com/) and [Heroku](https://heroku.com/) concepts before
deploying this app.

Application configuration is in `app.json` and you should be able to deploy using
If you're unable to successfully deploy using the button you will need to try using the CLI.

## Deployment by using [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli):

### Create a new Heroku App.

<div>

    create app__warframe_ds

</div>

### Add buildpacks

<div>

    heroku buildpacks:add --index=1 heroku/python

</div>

### Deploy on Heroku by pushing to the `heroku` branch

<div>

    git push heroku master

</div>


# Disclaimer:
<p>

    I do not claim to own either Warframe Marketplace or WarFrame those are IP of their respective
    companies/organizations.
    I'm just a fan of the game and would like to work on a project for school that I have Domain knowledge about. this
    app is the result of that project

</p>
