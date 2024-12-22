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
                    // Build the Docker image for the website
                    sh 'docker build -t my-static-website .'
                }
            }
        }

        stage('Run Website in Docker') {
            steps {
                script {
                    // Run the container and wait for it to be ready
                    sh '''
                        docker run -d --name my-static-website-container -p 8081:80 my-static-website

                        # Wait for the container to start responding
                        for i in {1..15}; do
                            if curl -s http://localhost:8081 > /dev/null; then
                                echo "Website is up!"
                                exit 0
                            fi
                            echo "Waiting for website to be up..."
                            sleep 2
                        done
                        echo "Website failed to start. Logs from container:"
                        docker logs my-static-website-container
                        exit 1
                    '''
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
                    echo "Website is running on port 8081."
                    // Add further deployment steps if required
                }
            }
        }
    }

    post {
        always {
            script {
                // Cleanup Docker resources
                sh '''
                    docker ps -a -q | xargs -r docker rm -f
                    docker images -f "dangling=true" -q | xargs -r docker rmi -f
                '''
            }
        }
    }
}

