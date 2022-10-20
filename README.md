# [Ultraviolence.py](https://github.com/MaryM12/Python_BI_2022/blob/homework3_modules_environments/ultraviolence.py) Running Instructions 
Hi! Here I provide the instructions on how to run **[Ultraviolence.py](https://github.com/MaryM12/Python_BI_2022/blob/homework3_modules_environments/ultraviolence.py)** script on the example of WSL on Windows 10. 

OS VERSION
------------
Ubuntu on Windows (WSL on Windows 10)

Distributor ID: Ubuntu
Description:    Ubuntu 20.04.5 LTS
Release:        20.04
Codename:       focal

PYTHON VERSION
------------
Python3.11

PACKAGE INSTALLATION
------------
The required packages are listed in requirements.txt file. However, you can find step-by-step instructions
on their installation and the whole workflow in the next section.

EXAMPLE
------------
Create and activate virtual environment with Python3.11:

```
sudo apt install python3.11 python3.11-venv
python3.11 -m venv virt2
source ./virt2/bin/activate
```
Install the requiered packages with pip:
```
pip install --upgrade google-api-python-client
pip install --upgrade pip
pip install beautifulsoup4
pip install pandas==1.4.4
sudo apt-get install python3.11-dev
sudo apt install build-essential
pip install biopython
pip install aiohttp
pip install opencv-python
pip install lxml
```
Run the script:
```
python3.11 ultraviolence.py
```

**You are doing great!**

