!# /bin/bash
cd
rm -rf task
docker rm -f $(docker ps -a -q)
docker rmi $(docker images -a -q)