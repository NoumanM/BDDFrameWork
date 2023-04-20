## **Python Behave BDD Framework**

This is a BDD automation framework developed on Selenium and Python Behave.
Sample test side used in this project is - website_url

Page Object Model is followed in this framework

**pages** folder contains the elements and corresponding actions of the pages

**features** folder contains **steps** folder which has all the test files and also the feature files.

**drivers** directory contains the chrome and firefox driver for mac

**requirements.txt** file contains all the python packages needed to run this framework

**allure** directory contains the files generated with allure reports

### **Commands to run the tests**

**To run the test with allure report**
` behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features -D url=website_url`
' behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features -D url=website_url'

**To run the test without allure report** 
`behave features`

**To run the test with allure report in parallel**
  python ./behave_parallel.py "-D url=website_url" 
  python ./behave_parallel.py "-D url=website_url"


### **Commands to run the tests on docker for beta**
** docker-compose -f docker-compose.yml build
** docker-compose -f docker-compose.yml up --exit-code-from Smoke_Test

### **Commands to run the tests on docker for alpha**
** docker-compose -f docker-compose-alpha.yml build
** docker-compose -f docker-compose-alpha.yml up --exit-code-from Smoke_Test