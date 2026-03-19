pipeline {
    agent any
    
    environment {
        PROJECT_NAME = 'Student Feedback Form'
        PYTHON_VERSION = 'python'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo "======================================"
                echo "Stage 1: Checking out source code"
                echo "======================================"
                // Git checkout happens automatically if configured
                echo "✓ Code checkout complete"
            }
        }
        
        stage('Environment Setup') {
            steps {
                echo "======================================"
                echo "Stage 2: Setting up environment"
                echo "======================================"
                script {
                    if (isUnix()) {
                        sh '''
                            echo "Checking Python version..."
                            python3 --version
                            echo "Installing Selenium..."
                            pip3 install selenium
                        '''
                    } else {
                        bat '''
                            echo Checking Python version...
                            python --version
                            echo Installing Selenium...
                            pip install selenium
                        '''
                    }
                }
                echo "✓ Environment setup complete"
            }
        }
        
        stage('Run Selenium Tests') {
            steps {
                echo "======================================"
                echo "Stage 3: Running Selenium test suite"
                echo "======================================"
                script {
                    if (isUnix()) {
                        sh 'python3 test_feedback_form.py'
                    } else {
                        bat 'python test_feedback_form.py'
                    }
                }
                echo "✓ Test execution complete"
            }
        }
        
        stage('Validate Results') {
            steps {
                echo "======================================"
                echo "Stage 4: Validating test results"
                echo "======================================"
                echo "✓ All tests completed"
                echo "Check console output for detailed results"
            }
        }
    }
    
    post {
        always {
            echo "======================================"
            echo "Build Complete"
            echo "======================================"
            echo "Project: ${PROJECT_NAME}"
            echo "Build Number: ${BUILD_NUMBER}"
            echo "Build Status: ${currentBuild.currentResult}"
        }
        success {
            echo "✓✓✓ BUILD SUCCESS ✓✓✓"
            echo "All tests passed successfully!"
        }
        failure {
            echo "✗✗✗ BUILD FAILED ✗✗✗"
            echo "One or more tests failed. Check console output for details."
        }
        unstable {
            echo "⚠ BUILD UNSTABLE ⚠"
            echo "Build completed but may have issues."
        }
    }
}
