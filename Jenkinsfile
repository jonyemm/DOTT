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
                   sh "/home/jenkins/tools/hudson.plugins.sonar.SonarRunnerInstallation/sonarqubescanner/bin/sonar-scanner 
                       -Dsonar.host.url=http://44.202.97.152:9000/ -Dsonar.projectName=DOTTPYTHON 
                       -Dsonar.projectVersion=1.0 -Dsonar.projectKey=DOTTPYTHON -Dsonar.sources=. -Dsonar.projectBaseDir=/home/jenkins/workspace/Python"
                }
            }
        }
    }
}

