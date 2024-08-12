## Install project
1. Clone repo
```
git clone https://github.com/bkochedikov/pythonSelenium.git
```
2. Cd into directory
```
cd pythonSelenium/
```
3. Instal requirements.txt
```
sudo apt install python3
sudo apt install python3-pip
pip install -r requirements.txt
```
## How to use

Run tests on chrome browser
```
python3 -m pytest
```
Run tests on firefox browser
```
python3 -m pytest --browser firefox
```
Run tests in multiple threads 
```
python3 -m pytest -n2 (2 threads)
```

## Allure
To use with allure install it and use commands
```
python3 -m pytest --alluredir=report
allure serve report
```
