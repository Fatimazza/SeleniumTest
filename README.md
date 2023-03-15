<h1 align="center">Selenium Test</h1></br>

<p align="center">
:sparkles: Web Automation Testing using Selenium WebDriver &amp; Python :sparkles:
</p>

## Preparation

What will be used on this project


| Item           | Source                                                         |
| -------------- | ------------------------------------------------------------ |
| Editor         | VS Code (https://code.visualstudio.com/download) |
| Package Manager| PIP (https://pip.pypa.io/en/stable/getting-started/) |
| UI Test Tools  | Selenium WebDriver with Python (https://pypi.org/project/selenium/) |
|                | WebDriver Manager (https://pypi.org/project/webdriver-manager/) |
| Browser        | Latest version of Chrome / Mozilla Firefox  |


## Pre-Requisite Installation

Install VS Code Editor, Python, and PIP

To check whether you already installed Python & PIP

```Bash
python --version
```
```Bash
python -m pip --version 
```

## Testing Tools Installation

Install Selenium

```Bash
python -m pip install Selenium
```

Install Web Driver Manager

```Bash
python -m pip install webdriver-manager
```

## Setting up Project

### Clone

**👉 [Clone this Repository](https://github.com/Fatimazza/SeleniumTest/)** through Terminal or Command Prompt

### Open the Project on Editor

Open this Automation Project using VS Code Editor.

### Run the Automation Project 

Change to Project directory on Terminal or Command Prompt

```Bash
cd SeleniumTest
```

Run All Tests on Terminal

> Note: Only for file which name started with `test_`

```Bash
python -m unittest
```

Run Specific Test 

```Bash
python -m unittest test_pythonorg.py
```

```Bash
python -m unittest test_saucedemo.py
```

Run Specific Test Case 

```Bash
python test_saucedemo.py TestSauceDemo.test_e_success_logout
```
