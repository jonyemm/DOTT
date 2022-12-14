pipeline {
    agent {
        docker { image 'jonathanemmanuel96/python_dott:latest' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'python -m py_compile cidr_convert_api/python/api.py'
                stash (name: 'compiled-results', includes: 'cidr_convert_api/python/api.py')
            }
        }

        stage ('Analysis'){
            steps{
                withSonarQubeEnv(installationName: 'sq1'){
                    echo 'im in'
		    sh "${ tool ("sonar-scanner")}/sonar-scanner -Dproject.settings=sonar-scanner.properties"
                }
            }
        }
    }
}

