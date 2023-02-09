# **SpyderBot**

SpyderBot is a simple Python script designed to spider a website and gather all its internal links. The links are stored in a text file for future reference.

### **Requirements**

To run SpyderBot, you need to have the following software installed:

* Python 3.x
* pip
* requests
* bs4

### **Installation**

To install SpyderBot, simply clone the repository using the following command:
`git clone https://github.com/meeranh/SpyderBot.git`

### **Usage**

The following command-line arguments can be used with SpyderBot:

`python main.py --help`

This will display the available command-line arguments:

`
usage: main.py [-h] [--scope SCOPE] url

Spider a website

positional arguments:
  url                   Full URL to spider (e.g. https://www.youtube.com)

optional arguments:
  -h, --help            show this help message and exit
  --scope SCOPE, -s SCOPE
                        Scope of the spider
`

Example:

`python main.py https://www.example.com`

### **Output**

The internal links of the spidered website will be stored in a file called `'links.txt'` in the same directory as the script.
