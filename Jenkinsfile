pipeline {
    agent any
    
    environment {
        PROJECT_NAME = 'Student Feedback Form'
        CI = 'true'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '======================================'
                echo 'Stage 1: Checking out source code'
                echo '======================================'
                echo '[DONE] Code checkout complete'
            }
        }
        
        stage('Environment Setup') {
            steps {
                echo '======================================'
                echo 'Stage 2: Setting up Python virtual environment'
                echo '======================================'
                script {
                    if (isUnix()) {
                        sh '''
                            echo "Checking Python version..."
                            python3 --version
                            
                            echo "Creating virtual environment..."
                            python3 -m venv venv
                            
                            echo "Activating venv and installing dependencies..."
                            . venv/bin/activate
                            pip install --upgrade pip
                            pip install selenium webdriver-manager
                            
                            echo "[DONE] Environment setup complete"
                        '''
                    } else {
                        // Windows PowerShell
                        powershell '''
                            Write-Host "Checking Python version..."
                            python --version
                            
                            Write-Host "Creating virtual environment..."
                            python -m venv venv
                            
                            Write-Host "Activating venv and installing dependencies..."
                            .\\venv\\Scripts\\Activate.ps1
                            
                            python -m pip install --upgrade pip
                            pip install selenium webdriver-manager
                            
                            Write-Host "[DONE] Environment setup complete"
                        '''
                    }
                }
            }
        }
        
        stage('Run Selenium Tests') {
            steps {
                echo '======================================'
                echo 'Stage 3: Running Selenium test suite (headless)'
                echo '======================================'
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            python test_feedback_form.py --headless
                        '''
                    } else {
                        // Windows PowerShell
                        powershell '''
                            .\\venv\\Scripts\\Activate.ps1
                            python test_feedback_form.py --headless
                        '''
                    }
                }
                echo '[DONE] Test execution complete'
            }
        }
        
        stage('Validate Results') {
            steps {
                echo '======================================'
                echo 'Stage 4: Validating test results'
                echo '======================================'
                echo '[DONE] All tests completed'
                echo 'Check console output for detailed results'
            }
        }
    }
    
    post {
        always {
            echo '======================================'
            echo 'Build Complete'
            echo '======================================'
            echo "Project: ${PROJECT_NAME}"
            echo "Build Number: ${BUILD_NUMBER}"
            echo "Build Status: ${currentBuild.currentResult}"
            
            // Clean up venv (optional)
            script {
                if (isUnix()) {
                    sh 'rm -rf venv || true'
                } else {
                    powershell 'Remove-Item -Recurse -Force venv -ErrorAction SilentlyContinue'
                }
            }
        }
        success {
            echo '=== BUILD SUCCESS ==='
            echo 'All tests passed successfully!'
        }
        failure {
            echo '=== BUILD FAILED ==='
            echo 'One or more tests failed. Check console output for details.'
        }
        unstable {
            echo '=== BUILD UNSTABLE ==='
            echo 'Build completed but may have issues.'
        }
    }
}
