1. Test Plan Information

Project Name: UI Automation Demo
Author: Taranovskyi Serhii
Date: 2026‑02‑24
Version: 1.0
Testing Scope: Login Page and Dashboard Page

Test Types:
	•	Functional Testing (positive and negative login)
	•	UI Testing (menu and table visibility)
	•	Regression Testing (to verify future changes don’t break existing functionality)

Test Environment:
	•	OS: macOS
	•	Browser: Chrome (Selenium WebDriver)
	•	Base URL: http://127.0.0.1:5000/login
	•	Maximum wait for UI elements: 10 seconds

2. Objectives
	•	Verify that Login Page functions correctly with valid and invalid credentials.
	•	Verify that Dashboard Page displays menu and table after successful login.
	•	Ensure error messages appear on failed login attempts.

3. Test Scope

In Scope
	•	Positive login (admin/admin)
	•	Negative login (wrong username/password)
	•	Dashboard menu visibility
	•	Dashboard table visibility and non-empty check

Out of Scope
	•	Logout functionality
	•	User registration
	•	Security testing
	•	Performance testing

4. Entry Criteria
	•	Application is deployed locally at 127.0.0.1:5000
	•	Selenium WebDriver is installed and configured
	•	Python dependencies installed via requirements.txt

5. Exit Criteria
	•	All planned test cases executed
	•	All critical and high-severity bugs reported
	•	No untested mandatory functional requirement

6. Test Approach / Strategy
	•	Functional Testing:
Use pytest + Selenium to execute UI test cases for Login and Dashboard.
	•	Positive Testing:
Validate correct login, dashboard menu, and table display.
	•	Negative Testing:
Validate incorrect login credentials show error messages.
	•	Regression Testing:
After each change, rerun all automated tests to ensure Dashboard and Login continue to work.

7. Test Deliverables
	•	Test Plan (test-plan.md)
	•	Test Cases (test-cases/)
	•	Checklist (checklist.md)
	•	Bug Reports (bug-reports/)
	•	Automated test scripts (tests/)

8. Risks & Assumptions
	•	Risk: Application may change URL or element IDs, breaking tests.
	•	Risk: Slow page load may cause timeout failures in Selenium.
	•	Assumption: Only admin user exists with credentials admin/admin.
	•	Assumption: Dashboard always contains at least one row in the table.
