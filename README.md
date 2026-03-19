# Student Feedback Registration Form - DevOps CA-2

A comprehensive student feedback registration system with automated testing and CI/CD integration.

## Project Overview

This project implements a Student Feedback Registration Form with:
- HTML5 form structure
- Brutalist CSS design system
- JavaScript validation
- Selenium automated testing
- Jenkins CI/CD integration

## Project Structure

```
CA-2/
├── index.html              # Main HTML form
├── styles.css              # External CSS (brutalist design)
├── validation.js           # JavaScript validation logic
├── test_feedback_form.py   # Selenium test suite
├── Jenkinsfile            # Jenkins pipeline configuration
├── README_JENKINS.md      # Jenkins setup guide
├── README_SELENIUM.md     # Selenium testing guide
└── TASK.md               # Original task requirements
```

## Features

### Form Fields
- Student Name (required)
- Email ID (required, validated)
- Mobile Number (required, 10 digits)
- Department (dropdown selection)
- Gender (radio buttons)
- Feedback Comments (required, min 10 words)
- Submit and Reset buttons

### Validation Rules
- Student Name: Cannot be empty
- Email: Must be in valid email format
- Mobile: Must be exactly 10 digits
- Department: Must be selected from dropdown
- Gender: One option must be selected
- Feedback: Minimum 10 words required

### Design System
- **Style**: Brutalist, sharp, minimal
- **Typography**: Courier New monospace
- **Colors**: Black, white, yellow accents
- **Borders**: Bold 3-4px solid borders
- **Shadows**: Sharp box shadows for depth
- **No transitions**: Instant state changes

## Git Branches

Each sub-task is implemented in a separate branch:

- `master` - Main branch with task requirements
- `subtask-1-html-form` - HTML form structure
- `subtask-2-css-styling` - CSS styling (internal & external)
- `subtask-3-javascript-validation` - JavaScript validation
- `subtask-4-selenium-tests` - Selenium test suite
- `subtask-5-jenkins-automation` - Jenkins integration

## Getting Started

### Prerequisites

1. **Web Browser** (Chrome, Firefox, Edge, Safari)
2. **Python 3.x** (for Selenium tests)
3. **Selenium WebDriver** (`pip install selenium`)
4. **ChromeDriver** (matching your Chrome version)
5. **Jenkins** (optional, for CI/CD)

### Running the Form

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CA-2
   ```

2. Open `index.html` in your web browser:
   ```bash
   # Windows
   start index.html
   
   # Mac
   open index.html
   
   # Linux
   xdg-open index.html
   ```

### Running Tests

1. Install Selenium:
   ```bash
   pip install selenium
   ```

2. Run the test suite:
   ```bash
   python test_feedback_form.py
   ```

### Jenkins Integration

See `README_JENKINS.md` for detailed Jenkins setup instructions.

## Test Coverage

The Selenium test suite includes 7 comprehensive test cases:

1. ✓ Page loads successfully
2. ✓ Valid form submission
3. ✓ Empty fields validation
4. ✓ Invalid email validation
5. ✓ Invalid mobile validation
6. ✓ Dropdown selection
7. ✓ Button functionality

## Technologies Used

- **HTML5** - Form structure
- **CSS3** - Styling and design
- **JavaScript (ES6)** - Client-side validation
- **Python 3** - Test automation
- **Selenium WebDriver** - Browser automation
- **Jenkins** - CI/CD automation
- **Git** - Version control

## Development Workflow

1. Each sub-task is developed in its own branch
2. All branches start from the `master` branch
3. Commits follow semantic commit messages
4. Tests are run before merging
5. Jenkins automates the testing process

## Branch Checkout Guide

To view a specific sub-task implementation:

```bash
# Sub Task 1: HTML Form
git checkout subtask-1-html-form

# Sub Task 2: CSS Styling
git checkout subtask-2-css-styling

# Sub Task 3: JavaScript Validation
git checkout subtask-3-javascript-validation

# Sub Task 4: Selenium Tests
git checkout subtask-4-selenium-tests

# Sub Task 5: Jenkins Automation
git checkout subtask-5-jenkins-automation
```

## Validation Examples

### Valid Submission
- Name: "John Doe"
- Email: "john.doe@example.com"
- Mobile: "9876543210"
- Department: "Computer Science"
- Gender: "Male"
- Feedback: "This form is excellent and provides great user experience with proper validation."

### Invalid Submissions
- Empty name: ✗ "Student name is required"
- Invalid email: ✗ "Invalid email format"
- Short mobile: ✗ "Enter valid 10-digit mobile number"
- No department: ✗ "Please select a department"
- No gender: ✗ "Please select a gender"
- Short feedback: ✗ "Minimum 10 words required"

## Browser Compatibility

Tested and working on:
- Chrome 90+
- Firefox 88+
- Edge 90+
- Safari 14+

## Contributing

This is a student project for DevOps CA-2. Contributions follow the assignment requirements.

## License

This project is created for educational purposes as part of DevOps coursework.

## Author

Singapore Institute of Technology - DevOps CA-2

## Acknowledgments

- Task requirements provided by instructor
- Brutalist design inspiration from modern web design trends
- Selenium documentation for test automation patterns
