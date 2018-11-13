#!/bin/sh
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
#heroku plugins:install heroku-container-registry
heroku login
heroku plugins:install @heroku-cli/plugin-container-registry
#docker login -u $DOCKER_EMAIL --password=$HEROKU_API_KEY registry.heroku.com 
heroku container:login
heroku container:push web --app $HEROKU_APP_NAME