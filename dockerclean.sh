!# /bin/bash
cd
rm -rf task
docker rm -f $(docker ps -a -q)
docker rmi $(docker images -a -q)
git clone https://github.com/tsmabbas/task.git
cd task/task
# docker build . --build-arg SECRET_KEY=${SECRET_KEY} --build-arg DATABASE_URI=${DATABASE_URI} -t myappi
# docker run -d -p 5000:5000 --name myappc myappi
# docker run -d -p 5000:5000 --env SECRET_KEY=${SECRET_KEY} --env DATABASE_URI=${DATABASE_URI} --name myappc myappi
