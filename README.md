# NGINX single webserver - running in Docker 

Send API calls (no auth) to the server. They will be displayed on the webpage. For example, on the CLI:   
 -  `curl -k -X POST -H "Content-Type: application/json" -d '{"mic-check":"123"}' https://10.233.10.182/api/data`  
  
To build & run:  
 1.) Build with: `docker-compose --verbose build`  
 2.) Start with: `docker-compose up -d`  
  
 Re-run steps if any chnages are made to code. Changes are non-persistent and reset on each new `docker-compose up -d`
