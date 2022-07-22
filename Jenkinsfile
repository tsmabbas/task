pipeline{
        agent any
        stages{
            stage('Clone Source'){
                steps{
                    sh "rm -rf task"
                    sh "git clone https://github.com/tsmabbas/task.git"
                    sh "cd task"
                    sudo chmod 666 /var/run/docker.sock
                    sh "docker compose up"

                }
            }
            
}
}