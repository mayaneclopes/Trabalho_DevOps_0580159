pipeline {
    agent any

    stages {
        stage('Verificar Ambiente') {
            steps {
                script {
                    if (!fileExists('requirements.txt')) {
                        error "requirements.txt não encontrado."
                    }
                    sh 'python3 --version'
                    sh 'pip3 --version'
                }
            }
        }
        
        stage('Clonar Repositório') {
            steps {
                git branch: 'main', url: 'https://github.com/mayaneclopes/Trabalho_DevOps_0580159.git'
            }
        }

        stage('Instalar Dependências') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Rodar Testes') {
            steps {
                sh 'pytest --no-cache -v'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}


