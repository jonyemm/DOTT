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
                    echo 'im in SQ'
		    sh '''$SCANNER_HOME/bin/sonar-scanner \
         	    -Dsonar.projectKey=projectKey \
         	    -Dsonar.projectName=projectName \
         	    -Dsonar.sources=src/ \
         	    -Dsonar.java.binaries=target/classes/ \
         	    -Dsonar.exclusions=src/test/java/****/*.java \
         	    -Dsonar.java.libraries=/var/lib/jenkins/.m2/**/*.jar \
         	    -Dsonar.projectVersion=${BUILD_NUMBER}-${GIT_COMMIT_SHORT}'''		
                }
            }
        }
    }
}

