🧪 UI Automation Demo Project

Demo project for UI test automation using Python + Pytest + Selenium WebDriver.

📌 Project Description

This project demonstrates automated UI testing of a simple web application with:
	•	Login functionality
	•	Dashboard page with table validation
	•	Page Object Model (POM) structure
	•	Pytest framework
	•	Selenium WebDriver
	•	Fixture-based driver management

The goal of this project is to showcase practical UI automation skills and clean project structure suitable for junior QA Automation roles.

⸻

🛠 Tech Stack
	•	Python 3.14
	•	Pytest
	•	Selenium WebDriver
	•	ChromeDriver
	•	Page Object Model (POM)

⸻

📂 Project Structure
ui-automation-demo/
│
├── app.py
├── conftest.py
├── pytest.ini
├── requirements.txt
│
├── pages/
│   ├── base_page.py
│   └── login_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_dashboard.py
│
└── utils/
    └── driver_factory.py

 🚀 How to Run the Project
 
 1. Clone repository :
 git clone https://github.com/kachaaaa/ui-automation-demo.git
 
 cd ui-automation-demo
 
 2. Create virtual environment :
 python -m venv .venv
 source .venv/bin/activate   # Mac/Linux
 
 3. Install dependencies : 
 pip install -r requirements.txt
 
 4. Run the applecation : 
 python app.py
 App will start at : http://127.0.0.1:5000

 5. Run tests :
 pytest -s

 ✅ Implemented Test Cases

🔐 Login Tests
	•	Valid login
	•	Invalid login validation

📊 Dashboard Tests
	•	Dashboard page loading
	•	Table presence validation
	•	Table rows validation

  📖 Design Patterns Used
	•	Page Object Model (POM)
	•	Fixture-based driver initialization
	•	Explicit waits (WebDriverWait)

  🎯 Purpose

This project is part of my QA Automation portfolio and demonstrates:
	•	Clean test structure
	•	Separation of concerns
	•	Reusable components
	•	Practical Selenium usage
