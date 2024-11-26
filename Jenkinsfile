pipeline {
    agent any

    stages {
        stage('Verificar Ambiente') {
            steps {
                sh 'which pytest'
                sh 'which docker'
            }
        }

        stage('Instalar Docker') {
            steps {
                sh 'apt-get update && apt-get install -y docker.io'
            }
        }

        stage('Instalar Dependências Python') {
            steps {
                sh 'pip install pytest'
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mayaneclopes/Trabalho_DevOps_0580159.git'
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
