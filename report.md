# Project 7 Report: Automated Testing with Pytest

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Pytest Version & Framework:**`, `**GitHub Repository URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information
- **Name:** Ei Ei Tun
- **MMDT ID:** MMDT026

---

## Section 1: Test Suite Configuration
- **Pytest Version & Framework:** Python 3.13.0, pytest 9.1.1, pytest-cov 7.1.0
- **Total Test Cases Written:** 147
- **Measured Code Coverage (%):** 95%
- **Key Fixtures Implemented:** I implemented two fixtures in tests/conftest.py: sample_student and student_manager. The sample_student fixture creates a sample Student object, while the student_manager fixture creates a fresh, empty StudentManager object for each test that uses it.
---

## Section 2: Test Case Design & Boundary Analysis
- **Calculator Boundary & Edge Cases:** I tested calculator functions using boundary and edge cases such as zero, negative numbers, empty lists, and invalid data types. I also tested minimum and maximum scores, prime number edge cases, factorial of zero, and negative exponents. I used pytest.raises to check that invalid inputs produce the expected exceptions.
- **Validator Exception Scenarios:** I tested the Data Validator functions using invalid email formats, weak passwords, invalid usernames, and ages outside the allowed range. I also tested missing registration fields and incorrect data types. I used pytest.raises to verify that the functions raised the expected exceptions, such as InvalidEmailError, WeakPasswordError, InvalidUsernameError, InvalidAgeError, ValidationError, and TypeError.
- **Student Manager State Transitions:** I tested Student Manager operations such as adding students, rejecting duplicate student IDs, updating grades, calculating GPA, and deleting students. I checked that the student count and records changed correctly after adding or removing students. I also tested missing student errors, GPA boundaries, top performers, and filtering students by GPA.

---

## Section 3: Local Verification & Feature Checklist
*Check the test modules and features you successfully implemented and verified locally by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Module 1: Calculator Unit Tests with Boundary & Type Assertions (`test_calculator.py`)
- [x] Parameterized Testing with `@pytest.mark.parametrize` for Multiple Input Scenarios
- [x] Module 2: Data Validator Tests with Custom Exception Assertions (`pytest.raises`)
- [x] Module 3: Student Management System Tests with State Mutation & CRUD Verification
- [x] Reusable Pytest Fixtures in `conftest.py` for Modular Test Setup
- [x] Mutation Testing & Bug Detection Verification (Catching Hidden Mutants)
- [x] Code Coverage Analysis with `pytest-cov` (>= 85% Coverage)

---

## Section 4: Deployed and Presentation Information
- **GitHub Repository URL:** https://github.com/EiEiTun-Chula/TEST_MMDT026
- **Video Presentation Link:** https://drive.google.com/file/d/1AvoO_mrGXuNioEcMhqcQhS3Wzdbo7egt/view?usp=sharing

---

## Section 5: Discussion
*Provide your written analysis for each point by replacing the bracket placeholders below:*
- **Explain why a test suite that passes 100% does not guarantee code correctness, and how mutation testing or evaluating tests against buggy code verifies test suite effectiveness.**
    Even if all tests pass, it does not mean the program is completely correct. Some bugs may remain undetected because the tests cannot cover every possible situation. Mutation testing introduces small changes into the source code to check whether the tests can detect errors. If the tests fail because of these changes, it shows that the test suite can detect those faults.
- **Compare classical unit and integration testing in software engineering with modern AI engineering evaluation (e.g., LLM benchmarks, unit testing AI agents/tool calls, and Process Reward Models / LLM-as-a-judge).**
    In traditional software testing, unit testing checks individual functions, while integration testing checks whether different parts of a program work together correctly. In AI engineering, testing is different because AI models may give different answers to the same question. AI evaluation uses methods such as LLM benchmarks, agent testing, LLM-as-a-judge, and Process Reward Models to check the performance, accuracy, and quality of AI systems.