pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                sh 'echo "Setting up environment..."'
                // Установка зависимостей, если это необходимо
            }
        }
        stage('Download Data') {
            steps {
                sh 'python3 scp/scripts/data_creation.py'
            }
        }
        stage('Preprocess Data') {
            steps {
                sh 'python3 scripts/model_preprocessing.py'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python3 scripts/model_preparation.py'
            }
        }
        stage('Test Model') {
            steps {
                sh 'python3 scripts/model_testing.py'
            }
        }
    }
    post {
        always {
            sh 'echo "Pipeline completed."'
        }
    }
}
