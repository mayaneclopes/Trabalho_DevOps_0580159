pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mayaneclopes/Trabalho_DevOps_0580159.git'
            }
        }

        stage('Instalar Dependências') {
            steps {
                sh 'apt-get update && apt-get install -y docker.io'
                sh 'pip install pytest'
            }
        }

        stage('Rodar Testes') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build e Deploy') {
            steps {
                sh 'docker build -t sua-imagem .'
                sh 'docker run -d -p 8080:8080 sua-imagem'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizada'
        }
    }
}
