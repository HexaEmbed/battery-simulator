pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r backend/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh './venv/bin/python -m unittest discover tests'
            }
        }
        stage('Deploy to Raspberry Pi') {
            steps {
                sshagent(['raspberrypi-ssh']) {
                    sh '''
                    scp -o StrictHostKeyChecking=no -r backend frontend debian@192.168.137.23:/home/debian/battery-simulator
                    ssh -o StrictHostKeyChecking=no debian@192.168.137.23 "sudo systemctl restart battery-simulator.service"
                    '''
                }
            }
        }
    }
}
