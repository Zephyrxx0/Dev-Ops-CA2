# Jenkins Configuration for Student Feedback Form Testing

This guide will help you set up Jenkins to automate the execution of Selenium test cases for the Student Feedback Registration Form.

## Prerequisites

Before setting up Jenkins, ensure you have:

1. **Java JDK** (Java 11 or higher)
2. **Python 3.x** installed
3. **Selenium WebDriver** installed (`pip install selenium`)
4. **Chrome Browser** and **ChromeDriver** installed
5. **Git** installed (for repository integration)

## Jenkins Installation

### Windows

1. Download Jenkins from: https://www.jenkins.io/download/
2. Choose "Windows" and download the installer (.msi file)
3. Run the installer and follow the setup wizard
4. Access Jenkins at `http://localhost:8080`
5. Unlock Jenkins using the initial admin password found at:
   ```
   C:\Program Files\Jenkins\secrets\initialAdminPassword
   ```
6. Install suggested plugins
7. Create your first admin user

### Linux/Mac

```bash
# Download and install Jenkins
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins

# Start Jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

## Initial Jenkins Configuration

### 1. Install Required Jenkins Plugins

Navigate to: `Manage Jenkins` > `Manage Plugins` > `Available`

Install the following plugins:
- **Git Plugin** (for GitHub integration)
- **Pipeline Plugin** (for pipeline jobs)
- **HTML Publisher Plugin** (for test reports)
- **Python Plugin** (optional, for better Python support)

### 2. Configure Python in Jenkins

1. Go to `Manage Jenkins` > `Global Tool Configuration`
2. Add Python installation
3. Or ensure system Python is accessible in Jenkins PATH

### 3. Configure ChromeDriver

Ensure ChromeDriver is in the system PATH or specify the path in your test script.

## Creating a Jenkins Job for Selenium Tests

### Method 1: Freestyle Project (Recommended for Beginners)

#### Step 1: Create New Job

1. From Jenkins dashboard, click "New Item"
2. Enter job name: `Student-Feedback-Form-Tests`
3. Select "Freestyle project"
4. Click "OK"

#### Step 2: Source Code Management

**Option A: Local Folder**
- Under "Source Code Management", select "None"
- You'll manually specify the project directory in build steps

**Option B: GitHub Repository**
- Select "Git"
- Enter Repository URL: `https://github.com/yourusername/your-repo.git`
- Add credentials if repository is private
- Specify branch: `*/subtask-4-selenium-tests` or `*/master`

#### Step 3: Build Configuration

Under "Build" section, click "Add build step" > "Execute Windows batch command" (Windows) or "Execute shell" (Linux/Mac)

**For Windows:**
```batch
@echo off
echo ====================================
echo Running Selenium Test Suite
echo ====================================

REM Navigate to project directory (if using local folder)
cd /d D:\Codes\SIT\DevOps\CA-2

REM Run Python tests
python test_feedback_form.py

echo ====================================
echo Test Execution Complete
echo ====================================
```

**For Linux/Mac:**
```bash
#!/bin/bash
echo "===================================="
echo "Running Selenium Test Suite"
echo "===================================="

# Navigate to project directory
cd /path/to/your/project

# Run Python tests
python3 test_feedback_form.py

echo "===================================="
echo "Test Execution Complete"
echo "===================================="
```

#### Step 4: Post-Build Actions (Optional)

Add post-build actions to:
- Archive test results
- Send email notifications
- Publish HTML reports

#### Step 5: Save and Build

1. Click "Save"
2. Click "Build Now" to execute the job
3. View build output in "Console Output"

### Method 2: Jenkins Pipeline (Advanced)

Create a `Jenkinsfile` in your project root:

```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                // Git checkout happens automatically
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'pip install selenium' // Use 'sh' for Linux/Mac
            }
        }
        
        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium test suite...'
                bat 'python test_feedback_form.py' // Use 'sh' for Linux/Mac
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
```

Then create a Pipeline job in Jenkins and point it to your repository.

## Configuring Build Triggers

You can configure Jenkins to run tests automatically:

### 1. Poll SCM (Check for code changes)
- In job configuration, under "Build Triggers"
- Check "Poll SCM"
- Enter schedule (e.g., `H/15 * * * *` to check every 15 minutes)

### 2. GitHub Webhook (Immediate trigger on push)
- In GitHub repository settings > Webhooks
- Add webhook URL: `http://your-jenkins-url:8080/github-webhook/`
- In Jenkins job, check "GitHub hook trigger for GITScm polling"

### 3. Scheduled Builds
- Check "Build periodically"
- Enter cron syntax (e.g., `H 2 * * *` for 2 AM daily)

## Understanding Build Results

### Build Success
- Green checkmark icon
- Exit code 0
- All tests passed

### Build Failure
- Red X icon
- Non-zero exit code
- One or more tests failed

### Build Status Indicators
- Blue ball: Success
- Red ball: Failure
- Yellow ball: Unstable
- Grey ball: Aborted/Not built

## Viewing Test Results

1. Click on build number (e.g., #1, #2)
2. Click "Console Output" to see detailed logs
3. Review test execution output
4. Check which tests passed/failed

## Troubleshooting

### Common Issues

**Issue 1: Python not found**
- Solution: Add Python to system PATH or specify full path in build command

**Issue 2: ChromeDriver not found**
- Solution: Ensure ChromeDriver is in PATH or update test script with explicit path

**Issue 3: Permission denied**
- Solution: Run Jenkins with appropriate permissions or adjust file permissions

**Issue 4: Display not found (Linux headless)**
- Solution: Use headless Chrome or install Xvfb

**Issue 5: Module not found (selenium)**
- Solution: Install selenium in correct Python environment used by Jenkins

## Best Practices

1. **Version Control**: Always commit test changes to Git
2. **Environment Isolation**: Use virtual environments for Python dependencies
3. **Headless Testing**: Configure Chrome to run in headless mode for CI/CD
4. **Test Reports**: Generate and archive test reports for history
5. **Notifications**: Set up email/Slack notifications for build results
6. **Parallel Execution**: For large test suites, configure parallel execution
7. **Clean Workspace**: Clean workspace before each build for consistency

## Running Jenkins Job

### Manual Execution
1. Open Jenkins dashboard
2. Find your job "Student-Feedback-Form-Tests"
3. Click "Build Now"
4. Wait for execution
5. Check console output for results

### Scheduled/Automatic Execution
- Jenkins will automatically trigger builds based on configured triggers
- Monitor dashboard for build notifications

## Expected Jenkins Output

When build is successful, console output should show:

```
Started by user Admin
Running in workspace D:\Jenkins\workspace\Student-Feedback-Form-Tests
[Student-Feedback-Form-Tests] $ cmd /c call C:\WINDOWS\TEMP\jenkins123.bat

====================================
Running Selenium Test Suite
====================================

============================================================
STUDENT FEEDBACK FORM - SELENIUM TEST SUITE
============================================================

=== TEST 1: Page Loads Successfully ===
✓ Page loaded successfully
✓ Form is visible

=== TEST 2: Valid Form Submission ===
✓ Form filled with valid data
✓ Form submitted successfully
✓ Success message displayed

... (more test output)

============================================================
TEST SUMMARY
============================================================
✓ Page Loads Successfully: PASSED
✓ Valid Form Submission: PASSED
✓ Empty Fields Validation: PASSED
✓ Invalid Email Validation: PASSED
✓ Invalid Mobile Validation: PASSED
✓ Dropdown Selection: PASSED
✓ Button Functionality: PASSED

============================================================
Total Tests: 7
Passed: 7
Failed: 0
Success Rate: 100.00%
============================================================

====================================
Test Execution Complete
====================================
Finished: SUCCESS
```

## Next Steps

1. Configure email notifications for build failures
2. Set up automated builds on code commit
3. Create separate jobs for different branches
4. Implement test result archiving
5. Set up build pipeline with multiple stages
6. Configure parallel test execution for performance

## Additional Resources

- Jenkins Documentation: https://www.jenkins.io/doc/
- Jenkins Pipeline: https://www.jenkins.io/doc/book/pipeline/
- Selenium with Jenkins: https://www.selenium.dev/documentation/
