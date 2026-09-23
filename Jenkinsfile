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
                // Replace with your Pi's SSH details
                sh 'scp -r backend frontend debian@192.168.137.120:/home/debian/battery-simulator'
                sh 'ssh debian@192.168.137.120 "cd battery-simulator && nohup ./venv/bin/python backend/app.py &"'
            }
        }
    }
}
