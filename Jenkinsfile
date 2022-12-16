pipeline {
 agent any
    environment {
        scannerHome = tool 'sonarqube';
    }
    stages {
            stage('Build') {
                steps {
                    sh '''
			  cd ./cidr_convert_api/python/  
			  docker build . -t mi_api 
		       '''
		
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

            stage ('Pytest') {
                agent { docker { image 'jonathanemmanuel96/python_dott:latest' } }
                steps{
                    sh 'python --version'
                    sh 'pip install pytest'
                    sh 'chmod +x cidr_convert_api/python/tests.py'
                    sh 'py.test --junitxml results.xml cidr_convert_api/python/tests.py'
                }
            }

            stage('Deploy'){
                steps{
                    sh '''
			docker tag mi_api:latest jonyemm/mi_api:latest
		       	docker push jonyemm/mi_api:latest
			'''
                }
            }
      }
    }
