pipeline {
    agent {
        docker { image 'jonathanemmanuel96/python_dott:latest' }
    }
    stages {
        stage('Build') {
            steps {
              	sh 'python --version'
		sh 'python -m py_compile cidr_convert_api/python/api.py'
            }
        }
    }
}

