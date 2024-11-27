pipeline {
    agent any

    stages {
        stage('Verificar Ambiente') {
            steps {
                script {
                    if (!fileExists('app/requirements.txt')) {
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
                sh 'pip install -r app/requirements.txt'
            }
        }

        stage('Rodar Testes') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                        sh 'docker build -t nome_da_imagem -f app/Dockerfile_flask .'
                        sh 'docker push nome_da_imagem'
                    }

                    sh 'docker run -d -p 5000:5000 nome_da_imagem'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
