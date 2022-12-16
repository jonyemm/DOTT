pipeline {
 agent any
    environment {
        scannerHome = tool 'sonarqube';
	DOCKERHUB_CREDENTIALS=credentials('dockerhub1')
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
		   withDockerRegistry([ credentialsId:DOCKERHUB_CREDENTIALS, url: "https://index.docker.io/v1/" ]){ 
                    sh '''
			cd ./cidr_convert_api/python/
			docker build -t dottpython .
			docker tag dottpython jonathanemmanuel96/dottpython
		       	docker login -u $DOCKERHUB_CREDENTIALS
			'''
			}
                }
            }
      }
    }
