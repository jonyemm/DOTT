pipeline {
    agent {
        docker { image 'jonathanemmanuel96/python_dott:latest' }
    }
    stages {
        stage('Build') {
            steps {
              	sh 'python --version'
		sh 'cd cidr_convert_api/python/'
		sh 'ls'
            }
        }
    }
}

