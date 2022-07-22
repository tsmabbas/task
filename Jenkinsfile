pipeline{
        agent any
        stages{
            stage('Clone Source'){
                steps{
                    sh "rm -rf task"
                    sh "git clone https://github.com/tsmabbas/task.git"
                    sh "cd task"
                    sh "docker compose up"

                }
            }
            
}
}