# Selenium Test Framework

## 📖 Description
This project is a Selenium-based test framework for automating web application testing. It includes example tests for login validation, purchase flow on saucedemo and Google search functionality, with configurations managed in a `config.yaml` file.

## ⚙️ Requirements
- Python 3.10 or higher
- Installed packages (from `requirements.txt`):
  - `selenium`
  - `pytest`
  - `pyyaml`
  - `faker` 

## 🛠 Installation

1. **Clone the repository:**
    git clone https://github.com/Nyaxize/web_testing_project.git

2. **Install dependencies:**
    pip install -r requirements.txt

3. **Download ChromeDriver:**
    Make sure to download the version matching your Google Chrome browser from ChromeDriver Downloads. (my chromium version "114.0.5735.90")
        Direct link to chromedriver: https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_win32.zip
    Place the chromedriver.exe file in a known location.

4. **Update config.yaml (if needed).**
    
## 📂 Project Structure

## 🚀 How to Run Tests
    Run a specific test:
        pytest tests/test_example.py -s

        
