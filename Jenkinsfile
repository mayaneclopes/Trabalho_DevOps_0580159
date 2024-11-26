pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mayaneclopes/Trabalho_DevOps_0580159.git'
            }
        }

        stage('Rodar Testes') {
            steps {
                sh 'python3 -m venv venv'  
                sh 'source venv/bin/activate'  


                sh 'pip install pytest'


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
