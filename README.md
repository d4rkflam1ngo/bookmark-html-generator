# Python Bookmark HTML Generator
A Python script which will generate html bookmark files which you can import into most web browsers.

### Currently Supported Features
* Automatically get the base64 encoded favicon and page title
* Generate browser-import compatable HTML bookmarks file ([example output](https://github.com/d4rkflam1ngo/bookmark-html-generator/blob/main/example-output.html))

### Requirements
* requests
* beautifulsoup4
* favicon

### Installation
1. Clone this repository using the command:
```
git clone https://github.com/d4rkflam1ngo/bookmark-html-generator && cd bookmark-html-generator
```
2. Install the script requirements using:
```
pip3 install -r requirements.txt
```
3. Run the script:
```
python3 script.py
```
4. Once you have finished creating your bookmarks. Hit 2 on the menu to generate a .html file.
5. Import the bookmarks into your faveourite browser.
