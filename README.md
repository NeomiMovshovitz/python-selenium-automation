# Selenium-Python Test Example

This repository contains UI testing project,
using Python, Selenium Webdriver and Page Object Model pattern.
validating different areas on www.BestBuy.com site.

# Requirements

* Python 3.7.X
* pip and setuptools
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Instalation

1. Download or clone the repository 
2. Open a terminal
3. Go to the project root directory
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment executing the following script: `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`

# Test Execution

1. Open a terminal
2. From the project root directory run: `pytest -v --html=results/report.html`

# Configuration

By default, tests will be executed in Chrome (normal mode). Preferences can be changed in "/data/config.yaml" file

# Results

To check the report, open the '/results/report.html' file once the execution has finished.


# Links
   
   [Selenium - Python Documentation](<https://selenium-python.readthedocs.io/>)
   
   [Webdriver Manager for Python](<https://github.com/SergeyPirogov/webdriver_manager>)
   
   
