pipeline {
    agent any
    
    parameters {
        string(name: 'Greeting', defaultValue: 'Hello', description: 'How should I greet the world?')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh "echo 'hello'"
                script{
                    def a = 'varibale '
                    println a + "groovy" 
              
                }
                echo "${params.Greeting} world!"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
