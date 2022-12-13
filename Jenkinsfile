pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                powershell 'python --version'
            }
        }
     }
}
