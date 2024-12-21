pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-static-website"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Shivam0519/Myrepo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}", ".")
                }
            }
        }

        stage('Run Website in Docker') {
            steps {
                script {
                    docker.run("${DOCKER_IMAGE}", "-d")  // Run the website in detached mode
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Build the Docker image for Selenium tests
                    def seleniumContainer = docker.build("selenium-tests", "--target selenium-tests .")
                    
                    // Run the Selenium tests
                    seleniumContainer.run()
                }
            }
        }

        stage('Deploy Website') {
            steps {
                // Add deployment steps (e.g., pushing to a cloud, server, etc.)
                echo "Deploying static website..."
            }
        }
    }

    post {
        always {
            // Clean up Docker containers after tests
            sh "docker ps -a -q | xargs docker rm -f"
        }
    }
}

