To run the redis on docker 
<br><code>docker-compose -f redis-docker-compose.yml up</code>

To stop the redis server on docker:
<br><code>docker-compose -f redis-docker-compose.yml down</code>

To run Redis CLI
<br><code>docker exec -it redis-docker redis-cli</code>

RUN insight open the link in browser
<br>http://localhost:5540

Note
on insight - to add local(docker redis DB use the IP instead of localhost)
