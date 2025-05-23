pipeline {
  agent any

  tools {
    // Name must match the one set under Global Tool Configuration
    sonarQube 'SonarScanner'
  }

  environment {
    // 'sonar-token' must match the Jenkins credential ID for your SonarQube token
    SONAR_TOKEN = credentials('sonar-token')
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv('SonarQube') {
          sh '''
            sonar-scanner \
              -Dsonar.projectKey=my-demo \
              -Dsonar.sources=. \
              -Dsonar.host.url=http://localhost:9000 \
              -Dsonar.login=$SONAR_TOKEN
          '''
        }
      }
    }
  }
}
