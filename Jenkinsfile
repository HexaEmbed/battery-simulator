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
                    ssh -o StrictHostKeyChecking=no debian@192.168.137.23 "
                        cd battery-simulator &&
                        if [ ! -d venv ]; then python3 -m venv venv; fi &&
                        ./venv/bin/pip install -r backend/requirements.txt &&
                        nohup ./venv/bin/python backend/app.py &
                    "
                    '''
                }
            }
        }
    }
}
