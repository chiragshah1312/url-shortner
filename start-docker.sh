# run bash start-docker.sh to create and start the docker on port 8000
sudo docker rm -f url_shortner_chirag
export ENVSHORTNER=PROD
sudo docker build --build-arg ENVSHORTNER=PROD  -t url_shortner_chirag .
sudo docker run -it -d -p 8000:8000 -v dal:/usr/src/app/dal --restart=always --name url_shortner_chirag url_shortner_chirag
