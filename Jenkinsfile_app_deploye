pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-static-website"
        NETWORK_NAME = "test-network"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Shivam0519/Myrepo.git'
            }
        }

        stage('Create Docker Network') {
            steps {
                script {
                    sh 'docker network create ${NETWORK_NAME} || true'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t my-static-website .'
                }
            }
        }

        stage('Run Website in Docker') {
            steps {
                script {
                    sh '''
                        docker run -d --name my-static-website-container --network=${NETWORK_NAME} -p 8081:80 my-static-website

                        # Wait for the container to be ready
                        until curl -s http://localhost:8081; do
                            echo "Waiting for website to be up..."
                            sleep 2
                        done
                    '''
                }
            }
        }

        stage('Deploy Website') {
            steps {
                script {
                    echo "Website is running on port 8081."
                }
            }
        }
    }

    post {
        success {
            script {
                echo "Website deployment successful. Triggering Selenium tests..."
                build job: 'Selenium-Tests-Job'
            }
        }

        failure {
            script {
                echo "Website deployment failed. Skipping Selenium tests."
            }
        }
    }
}
