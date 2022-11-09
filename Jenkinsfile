pipeline{

	agent any
	options {
		buildDiscarder(logRotator(numToKeepStr:'5'))
	}

	environment {
		DOCKERHUB_CREDENTIALS = credentials('credential-docker')
	}
  stages {
		stage('Build') {
		  steps {
			sh 'docker build -t akkaoui/fastapi-python:latest .'
		  }
		}
		
		stage('Login') {
		  steps {
			sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
		  }
		}
		
		stage('Push') {
		  steps {
			sh 'docker push akkaoui/fastapi-python:latest'
		  }
		}
	}
	post {
		always {
		    sh 'docker logout'
		}
	}

}
