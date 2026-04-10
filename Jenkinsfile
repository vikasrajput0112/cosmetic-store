pipeline {
    agent any

    environment {
        IMAGE_NAME = "cosmetic-store"
        DOCKERHUB_CREDENTIALS = "dockerhub-creds"
    }

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/vikasrajput0112/cosmetic-store.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag $IMAGE_NAME yourdockerhub/$IMAGE_NAME:latest'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push yourdockerhub/$IMAGE_NAME:latest'
                }
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop cosmetic || true
                docker rm cosmetic || true
                docker run -d -p 8000:8000 --name cosmetic yourdockerhub/$IMAGE_NAME:latest
                '''
            }
        }
    }
}
