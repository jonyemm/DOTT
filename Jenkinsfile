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

          stage('SonarQube analysis') {
    def scannerHome = tool 'sonarqube';
    withSonarQubeEnv('sonarqube') {
      sh "${scannerHome}/bin/sonar-scanner \
           -D sonar.login=admin \
           -D sonar.password=admin \
           -D sonar.projectKey=sonarqubetest \
           -D sonar.exclusions=vendor/**,resources/**,**/*.java \
      	   -D sonar.host.url=http://44.202.97.152:9000/"
    	  }
        }
    }
}

