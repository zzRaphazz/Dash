pipeline {
    agent any

    options {
        timeout(time: 3, unit: 'MINUTES') // Limite de 3 minutos para evitar travamentos
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/zzRaphazz/Dash.git'
            }
        }
        stage('Analise Estática') {
            steps {
                sh 'flake8 --ignore=W291,W293,W391 ./*.py || true'
            }
        }
        stage('Inclui Doc') {
            steps {
                sh 'sphinx-build -b html source/ build/'
            }
        }
        stage('Ambiente de teste') {
            steps {
                script {
                    // Usamos '.' para construir a imagem a partir da pasta raiz atual
                    docker.build('dash_test', '.')
                    sh 'docker rm -f dash_test || true'
                    sh 'docker run -d --name dash_test -p 8081:8081 dash_test:latest'
                }
            }
        }
        stage('Test') {
            steps {
                sh 'docker exec dash_test python -m pytest'
            }
        }
    }

    post {
        always {
            script {
                echo 'Finalizando testes e desligando o container dash_test...'
                sh 'docker stop dash_test || true'
                sh 'docker rm -f dash_test || true'
            }
        }
    }
}
