# Crystal 3. Deploy on server Ubuntu 18

## INSTALL PYTHON & PIP

`sudo add-apt-repository ppa:jonathonf/python-3.6`  

> if it gives  ***add-apt-repository: command not found***   than use: `sudo apt-get install software-properties-common`

**Put each command separatly, one by one**
```
sudo apt update
sudo apt install python3.6
sudo apt install python3.6-dev
sudo apt install python3.6-venv
sudo apt-get install python3-distutils
sudo apt-get install build-essential
wget https://bootstrap.pypa.io/get-pip.py
sudo python3.6 get-pip.py
sudo ln -s /usr/bin/python3.6 /usr/local/bin/python3
sudo ln -s /usr/local/bin/pip /usr/local/bin/pip3
sudo ln -s /usr/bin/python3.6 /usr/local/bin/python
```



## Install test_bibox

```
sudo apt-get install git-core
git clone https://github.com/volkovartem77/test_bibox.git
```


## Creating virtualenv using Python 3.6

```
sudo pip install virtualenv
virtualenv -p /usr/bin/python3.6 ~/test_bibox/venv
cd ~/test_bibox; . venv/bin/activate
pip install -r requirements.txt
```

## Start APP


```
python test.py
```
