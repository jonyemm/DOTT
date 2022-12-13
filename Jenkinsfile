pipeline {
    agent {
        node {
            label 'my_local_server'
            customWorkspace '/projects/'
        }
    }
    stages {
        stage('Checkout project') {
            steps {
                script {
                    git branch: "master",
                        credentialsId: 'my-credentials',
                        url: 'https://user@github.org/myproject/sample-repo.git'
                }
            }
        }
        stage('Installing packages') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Static Code Checking') {
            steps {
                script {
                    sh 'find . -name \\*.py | xargs pylint -f parseable | tee pylint.log'
                    recordIssues(
                        tool: pyLint(pattern: 'pylint.log'),
                        unstableTotalHigh: 100,
                    )
                }
            }
        }
    }
}
