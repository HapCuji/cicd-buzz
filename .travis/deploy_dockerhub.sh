#!bin/sh

docker login -u $DOCKER_USER -p $DOCKER_PASS

docker build -f Dockerfile -t $DOCKER_USER/cicd-buzz:$TRAVIS_BRANCH . # "." - empty arg
docker push $DOCKER_USER/cicd-buzz