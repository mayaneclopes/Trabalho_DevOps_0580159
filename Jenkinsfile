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
        sh 'apt-get update && apt-get install -y python3 python3-pip python3-venv docker.io'
        sh 'pip3 install pytest'
    }
}

stage('Rodar Testes') {
    steps {
        sh 'pytest -v'
    }
}
    }

    post {
        always {
            echo 'Pipeline finalizada'
        }
    }
}
