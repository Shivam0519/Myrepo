pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-static-website"
        SELENIUM_IMAGE = "selenium-tests"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Shivam0519/Myrepo.git'
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
                    // Run the container in detached mode
                    sh 'docker run -d --name my-static-website-container -p 8081:80 my-static-website'
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Build and run Selenium tests
                    sh '''
                        docker build -t selenium-tests --target selenium-tests .
                        docker run --rm selenium-tests
                    '''
                }
            }
        }

        stage('Deploy Website') {
            steps {
                script {
                    echo "Website is running on port 8080."
                    // Add further deployment steps if required
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up Docker containers and images
                sh '''
                    echo "Cleaning up Docker resources..."
                    docker ps -a -q | xargs -r docker rm -f
                    docker images -q | xargs -r docker rmi -f
                '''
            }
        }
    }
}

