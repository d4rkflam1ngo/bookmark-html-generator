# script.py - 08/06/2022 - https://github.com/d4rkflam1ngo/bookmark-html-generator/blob/main/script.py

# Import required modules
import time
import base64
from urllib import response
import favicon
import requests
import bs4

folderObjects = ""

# Get base64 encoded site icon.
def getIconBase64(url):
  icon = favicon.get(url)[-1] # Select the smallest icon (last item in array)
  response = requests.get(icon.url, stream=True)

  # Return the b64 encoded icon
  return "data:"+str(response.headers['Content-Type'])+";"+"base64,"+base64.b64encode(response.content).decode("utf-8")

# Get the page title for the bookmark name
def getPageTitle(url):
  response = requests.get(url)
  html = bs4.BeautifulSoup(response.text, features="html.parser")
  print (html.title.text)
  return html.title.text.decode("utf-8")

while True:

  # Menu
  menu_selection = input("1. Create Folder\n2. Done\n> ")
  if int(menu_selection) == 2: 
    break
  elif int(menu_selection) == 1:
    folderName = input("Please enter a folder name\n> ")
    formattedLinks = ""

    # Ask for links
    while True:
      link = {}
      linkUrl = input("Enter a link URL (Blank to stop)\n> ")
      if linkUrl == "":
        break
      if linkUrl[:8] != "https://" or linkUrl[:7] != "https://":
        linkUrl = "http://"+linkUrl
      link["url"] = linkUrl
      
      # Try and get the page title for the bookmark name. If not just use the URL
      try:
        link["name"] = getPageTitle(link["url"])
      except:
        link["name"] = link["url"]

      # Try and get the b64 encoded site icon. If not use nothing (browser will cache icon if not present)
      try:
        link["icon"] = getIconBase64(link["url"])
      except: 
        link["icon"] = ""

      # Add link to existing lists
      formattedLinks = formattedLinks + '\n\t\t\t<DT><A HREF="{}" ADD_DATE="{}" ICON="{}">{}</A>'.format(link["url"], round(time.time()), link["icon"], link["name"])
    # Create folder and add to current folders
    folderObjects = folderObjects+'\n\t\t<DT><H3 ADD_DATE="{}" LAST_MODIFIED="{}">{}</H3>\n\t\t<DL><p>{}\n\t\t</DL><p>'.format(round(time.time()), round(time.time()), folderName, formattedLinks)
    
# Add folders to overall bookmarks object
bookmarksObject = '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n<TITLE>Bookmarks</TITLE>\n<H1>Bookmarks</H1><DL><p>\n\t<DT><H3 ADD_DATE="{}" LAST_MODIFIED="{}" PERSONAL_TOOLBAR_FOLDER="true">Bookmarks</H3>\n\t<DL><p>{}\n\t</DL><p>\n</DL><p>'.format(round(time.time()), round(time.time()), folderObjects)
  
# Write bookmarks to file
bookmarks_file = open("./bookmarks.html", "w")
bookmarks_file.writelines(bookmarksObject)
