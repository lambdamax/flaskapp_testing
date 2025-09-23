# Flask App Testing

A simple Flask web application designed for testing various security vulnerabilities and web application testing methodologies.

## Table of Contents

- [Flask App Testing](#flask-app-testing)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Testing Objectives](#testing-objectives)
    - [Primary Testing Goals](#primary-testing-goals)
    - [Test Coverage Areas](#test-coverage-areas)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Running the Application](#running-the-application)
    - [Manual Testing](#manual-testing)
  - [Running Tests](#running-tests)
    - [Test Cases Included](#test-cases-included)
  - [Security Considerations](#security-considerations)
    - [Known Vulnerabilities](#known-vulnerabilities)
    - [Educational Purpose](#educational-purpose)
  - [License](#license)

## Overview

This Flask application serves as a testing environment for exploring web application security concepts, particularly Cross-Site Scripting (XSS) vulnerabilities and input handling. The project demonstrates both vulnerable and secure coding practices for educational purposes.

## Project Structure

```
flask_app_testing/
├── flaskapp.py          # Main Flask application
├── test_flaskapp.py     # Unit tests for the application
├── flask_output.log     # Application logs
├── LICENSE              # MIT License
├── README.md            # Project documentation
└── __pycache__/         # Python cache files
```

## Testing Objectives

### Primary Testing Goals

1. **Cross-Site Scripting (XSS) Testing**
   - Test for reflected XSS vulnerabilities in user input handling
   - Verify that malicious scripts are properly sanitized or escaped
   - Validate input/output encoding mechanisms

2. **Input Validation Testing**
   - Test various input formats and edge cases
   - Verify data storage and retrieval functionality
   - Test form submission and data persistence

3. **Server Response Testing**
   - Verify correct HTTP status codes
   - Test server startup and shutdown procedures
   - Validate API endpoint responses

4. **Security Best Practices**
   - Demonstrate secure vs. insecure coding patterns
   - Test input sanitization effectiveness
   - Evaluate potential attack vectors

### Test Coverage Areas

- **Functional Testing**: Basic CRUD operations, form submissions
- **Security Testing**: XSS injection attempts, malicious input handling
- **Integration Testing**: End-to-end workflow testing
- **Server Management**: Proper startup/shutdown procedures

## Features

- **Simple Web Interface**: Basic HTML forms for user interaction
- **Data Storage**: In-memory database simulation
- **Input Processing**: Store and retrieve user-submitted data
- **Security Testing**: Intentional vulnerability for testing purposes
- **Server Management**: Graceful shutdown capability
- **Automated Testing**: Comprehensive test suite with unittest

## Installation

1. **Clone or download the project files**

2. **Install required dependencies**:
   ```bash
   pip install flask requests
   ```

3. **Ensure Python 3.x is installed** (tested with Python 3.12+)

## Usage

### Running the Application

1. **Start the Flask server**:
   ```bash
   python flaskapp.py
   ```

2. **Access the application**:
   - Open your browser to `http://127.0.0.1:5000`
   - Use the web interface to store and retrieve input

3. **Available Endpoints**:
   - `GET /` - Home page with forms
   - `POST /store` - Store user input
   - `GET /get-stored-input` - Retrieve stored input
   - `POST /shutdown` - Gracefully shutdown server

### Manual Testing

1. Navigate to the home page
2. Enter text in the input form and submit
3. Click "View Stored Input" to see the stored data
4. Test with various inputs including HTML/JavaScript

## Running Tests

Execute the automated test suite:

```bash
python test_flaskapp.py
```

### Test Cases Included

1. **test_store_input()**: Verifies input storage functionality
2. **test_get_stored_input()**: Tests data retrieval and display
3. **test_reflected_xss()**: Security test for XSS vulnerabilities

The tests automatically:
- Start a Flask server in a separate thread
- Execute all test cases
- Gracefully shutdown the server
- Report test results

## Security Considerations

⚠️ **Warning**: This application contains intentional security vulnerabilities for educational purposes.

### Known Vulnerabilities

- **Cross-Site Scripting (XSS)**: The application uses `render_template_string()` without proper escaping
- **Input Validation**: Minimal input sanitization
- **Session Security**: Hardcoded secret key

### Educational Purpose

This project is designed to:
- Demonstrate common web vulnerabilities
- Provide a safe testing environment
- Teach secure coding practices through comparison
- Enable security testing methodology practice

**Do not deploy this application in a production environment.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Author**: mattsebastianh  
**Project Type**: Educational Security Testing  
**Flask Version**: Compatible with Flask 2.x+