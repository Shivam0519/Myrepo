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
                    // Run the website container and expose it on port 8081
                    sh '''
                        docker run -d --name my-static-website-container -p 8081:80 my-static-website
                        
                        # Wait for the container to be ready
                        until curl -s http://localhost:8081; do
                            echo "Waiting for website to be up..."
                            sleep 2
                        done
                    '''
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Build and run the Selenium tests container
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
}

