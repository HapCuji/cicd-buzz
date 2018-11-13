#!bin/sh

docker login -u $DOCKER_USER -p $DOCKER_PASS

if [$TRAVIS_BRANCH == "master"];	then
		TAG = "latest"
	else
		TAG = "$TRAVIS_BRANCH"
fi 

docker build -f Dockerfile -t $DOCKER_USER/cicd-buzz:$TAG . # "." - empty arg
docker push $DOCKER_USER/cicd-buzz