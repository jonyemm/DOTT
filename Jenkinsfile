pipeline {
    agent {
        docker { image 'jonathanemmanuel96/python_dott:latest' }
    }
    stages {
        stage('Building') {
            steps {
                sh 'python --version'
                sh 'python -m py_compile cidr_convert_api/python/api.py'
                stash (name: 'compiled-results', includes: 'cidr_convert_api/python/api.py')
            }
        }

        stage ('Test'){
            steps{
                sh 'py.test --verbose --junit-xml test-reports/results.xml '
            }
        }
    }
}

