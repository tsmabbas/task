pipeline{
        agent any
        stages{
            stage('Docker Swarm1'){
                steps{

                    sh "docker stack deploy -E SECRET_KEY=${SECRET_KEY} -E DATABASE_URI=${DATABASE_URI} --compose-file docker-compose.yaml taskstack"
                    // sudo -E SECRET_KEY=${SECRET_KEY} -E DATABASE_URI=${DATABASE_URI} docker-compose up -d
                    // sh "rm -rf task"
                    // sh "git clone https://github.com/tsmabbas/task.git"
                    // sh "cd task"
                    // sh "sudo chmod 666 /var/run/docker.sock"
                    // sh "docker compose up"
                    // #!/bin/bash

// git clone https://github.com/tsmabbas/task.git
// cd task
// sudo -E SECRET_KEY=${SECRET_KEY} -E DATABASE_URI=${DATABASE_URI} docker-compose up -d

                }
            }
            
}
}