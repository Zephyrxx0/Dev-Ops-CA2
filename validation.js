// Form Validation JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('feedbackForm');
    const submitBtn = document.getElementById('submitBtn');
    const resetBtn = document.getElementById('resetBtn');
    const successMessage = document.getElementById('successMessage');

    // Form submission handler
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Clear previous error messages
        clearErrors();
        
        // Validate all fields
        let isValid = true;
        
        if (!validateName()) isValid = false;
        if (!validateEmail()) isValid = false;
        if (!validateMobile()) isValid = false;
        if (!validateDepartment()) isValid = false;
        if (!validateGender()) isValid = false;
        if (!validateFeedback()) isValid = false;
        
        if (isValid) {
            // Show success message
            successMessage.style.display = 'block';
            
            // Log form data (in real scenario, send to server)
            console.log('Form submitted successfully!');
            console.log({
                studentName: document.getElementById('studentName').value,
                email: document.getElementById('email').value,
                mobile: document.getElementById('mobile').value,
                department: document.getElementById('department').value,
                gender: document.querySelector('input[name="gender"]:checked').value,
                feedback: document.getElementById('feedback').value
            });
            
            // Optional: Reset form after successful submission
            setTimeout(() => {
                form.reset();
                successMessage.style.display = 'none';
            }, 3000);
        } else {
            successMessage.style.display = 'none';
        }
    });

    // Reset button handler
    resetBtn.addEventListener('click', function() {
        clearErrors();
        successMessage.style.display = 'none';
    });

    // Real-time validation on blur
    document.getElementById('studentName').addEventListener('blur', validateName);
    document.getElementById('email').addEventListener('blur', validateEmail);
    document.getElementById('mobile').addEventListener('blur', validateMobile);
    document.getElementById('department').addEventListener('change', validateDepartment);
    document.querySelectorAll('input[name="gender"]').forEach(radio => {
        radio.addEventListener('change', validateGender);
    });
    document.getElementById('feedback').addEventListener('blur', validateFeedback);

    // Validation Functions

    function validateName() {
        const name = document.getElementById('studentName').value.trim();
        const nameError = document.getElementById('nameError');
        
        if (name === '') {
            nameError.textContent = 'Student name is required';
            return false;
        }
        
        nameError.textContent = '';
        return true;
    }

    function validateEmail() {
        const email = document.getElementById('email').value.trim();
        const emailError = document.getElementById('emailError');
        
        if (email === '') {
            emailError.textContent = 'Email is required';
            return false;
        }
        
        // Email format validation
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailPattern.test(email)) {
            emailError.textContent = 'Invalid email format';
            return false;
        }
        
        emailError.textContent = '';
        return true;
    }

    function validateMobile() {
        const mobile = document.getElementById('mobile').value.trim();
        const mobileError = document.getElementById('mobileError');
        
        if (mobile === '') {
            mobileError.textContent = 'Mobile number is required';
            return false;
        }
        
        // Mobile number validation (only digits, 10 digits)
        const mobilePattern = /^[0-9]{10}$/;
        if (!mobilePattern.test(mobile)) {
            mobileError.textContent = 'Enter valid 10-digit mobile number';
            return false;
        }
        
        mobileError.textContent = '';
        return true;
    }

    function validateDepartment() {
        const department = document.getElementById('department').value;
        const departmentError = document.getElementById('departmentError');
        
        if (department === '') {
            departmentError.textContent = 'Please select a department';
            return false;
        }
        
        departmentError.textContent = '';
        return true;
    }

    function validateGender() {
        const gender = document.querySelector('input[name="gender"]:checked');
        const genderError = document.getElementById('genderError');
        
        if (!gender) {
            genderError.textContent = 'Please select a gender';
            return false;
        }
        
        genderError.textContent = '';
        return true;
    }

    function validateFeedback() {
        const feedback = document.getElementById('feedback').value.trim();
        const feedbackError = document.getElementById('feedbackError');
        
        if (feedback === '') {
            feedbackError.textContent = 'Feedback is required';
            return false;
        }
        
        // Count words (minimum 10 words)
        const wordCount = feedback.split(/\s+/).filter(word => word.length > 0).length;
        if (wordCount < 10) {
            feedbackError.textContent = `Minimum 10 words required (current: ${wordCount})`;
            return false;
        }
        
        feedbackError.textContent = '';
        return true;
    }

    function clearErrors() {
        document.querySelectorAll('.error').forEach(error => {
            error.textContent = '';
        });
    }
});
