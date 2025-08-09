### 🚧  Project Status: In Progress 🚧
- This project is still a work in progress. Contributions, issues, and feedback are welcome!

# 💻 QA Automation for AutomationExercise.com
This is a comprehensive QA project for a sample e-commerce site, built using the Page Object Model (POM) design pattern. Covering **automated testing** using Python, Selenium WebDriver, and PyTest.

## 📝AutomationExercise Test Cases
You can find the detailed test cases here: [TestCase.md](./TestCase.md)

## 🧪 Features Covered
✅ Login/SignUp Page (Complete)  <br>
✅ Product Page (Framework Created)<br>
✅ Cart (Framework Created) <br>
✅ Contact Us<br>

## 🧱 Project Structure
<pre> <code> 📁qa-automation/
│
├── config/ # Test data & configuration
├── pages/ # POM classes (Base, Header,Login/SignUp, Product, Cart)
│   ├── base_page.py
│   ├── cart_page.py
│   ├── header_components.py
│   ├── home_page.py
│   ├── product_page.py
│   └── signup_login_page.py
├── tests/ # Pytest test files
│   ├── test_HomePage.py
│   └── test_SignupLogin.py
├── conftest.py # Test setup & fixtures
└── requirements.txt </code> </pre>

## 🛠 Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0080FF?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D7?style=for-the-badge&logo=visual-studio-code&logoColor=white)


## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/melatemarkos/qa-automation.git
cd qa-automation

# (Optional) Create and activate a virtual environment:
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
# Set up environment
pip install -r requirements.txt

# Run tests and generate report
pytest 

```

