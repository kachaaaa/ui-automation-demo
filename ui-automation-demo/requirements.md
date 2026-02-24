UI Automation Demo – Requirements Specification

1. System Overview

The system is a local web application available at:
http://127.0.0.1:5000/login

The application contains:
	•	Login Page
	•	Dashboard Page (after successful authentication)

These requirements are derived strictly from the existing automated UI tests.

2. Functional Requirements

2.1 Login Page

FR-LOGIN-01

The system shall provide a Login page accessible at:
http://127.0.0.1:5000/login

FR-LOGIN-02

The Login page shall contain:
	•	Username input field (name="username")
	•	Password input field (name="password")
	•	Submit button (button[type='submit'])

  FR-LOGIN-03

If a user enters:
	•	username = admin
	•	password = admin

and submits the form,
the system shall redirect the user to the Dashboard page.

FR-LOGIN-04

After successful login, the URL shall contain:
dashboard

FR-LOGIN-05

If a user enters invalid credentials (e.g., wrong username and password),
the system shall:
	•	prevent login
	•	display an error message with class:
  class="error"

  2.2 Dashboard Page

FR-DASH-01

After successful authentication, the system shall display the Dashboard page.

FR-DASH-02

The Dashboard page shall contain a menu element with:
id="main-menu"

FR-DASH-03

The Dashboard page shall contain an HTML table element:
<table>

FR-DASH-04

The table displayed on the Dashboard page shall contain at least one row:
<tr>

3. Constraints / Non-Functional Requirements
	•	The application runs locally on 127.0.0.1:5000
	•	UI behavior is validated via Selenium WebDriver
	•	Maximum wait time for UI elements: 10 seconds
