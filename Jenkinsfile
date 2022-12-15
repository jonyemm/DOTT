pipeline {
 agent any
    environment {
        scannerHome = tool 'sonarqube';
    }
    stages {
        stage('Build') {
        agent { docker { image 'jonathanemmanuel96/python_dott:latest' } }
            steps {
                sh 'python --version'
                sh 'python -m py_compile cidr_convert_api/python/api.py'
                stash (name: 'compiled-results', includes: 'cidr_convert_api/python/api.py')
            }
        }

        stage('SonarQube') {
            steps {
                withSonarQubeEnv(installationName: 'sq1') {
                 sh ''' ${scannerHome}/bin/sonar-scanner \
                        -Dsonar.organization=311 \
                        -Dsonar.projectKey=DOTT-PYTHON \
                        -Dsonar.sources=./cidr_convert_api/python/ \
                        -Dsonar.host.url=https://sonarcloud.io '''
                }

            }
          }
        }
    }

