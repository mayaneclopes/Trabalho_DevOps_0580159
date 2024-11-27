pipeline {
    agent any

    environment {
        IMAGE_NAME = 'mayaneclopes/nome_da_imagem:latest'
    }

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
                        sh "docker build -t ${IMAGE_NAME} -f app/Dockerfile_flask ."
                        sh "docker push ${IMAGE_NAME}"
                    }
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
