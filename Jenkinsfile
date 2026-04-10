pipeline {
    agent any

    environment {
        IMAGE_NAME = "cosmetic-store"
        DOCKERHUB_USER = "vikas0112"
        DOCKERHUB_CREDENTIALS = "dockerhub-creds"
    }

    stages {

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag $IMAGE_NAME $DOCKERHUB_USER/$IMAGE_NAME:latest'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push $DOCKERHUB_USER/$IMAGE_NAME:latest'
                }
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop cosmetic || true
                docker rm cosmetic || true
                docker run -d -p 8000:8000 --name cosmetic $DOCKERHUB_USER/$IMAGE_NAME:latest
                '''
            }
        }
    }
}
