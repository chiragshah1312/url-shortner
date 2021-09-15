# url-shortner
Shortens a given URL and stores it in sqlite db. Also caches the url in cache.py
Made using Falcon framework 

Run the below command to start the docker container
<br />```bash start-docker.sh```



After starting the docker hit the below API
<br />```POST ```
<br />```http://0.0.0.0:8000/shorten_url```
<br />```input json -> {"link": "https://www.google.com"}```



The shortened and origional URLs are stored in cache.py and also in sqlite DB.
Cache will persist until the server/docker is on
