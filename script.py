# Jamie Pegg - 08/06/2022 - bookmark_html_generator.py

# Import required modules
import time
import favicon
import requests
import base64

folder_objects = ""

# Get base64 encoded site icon.
def getIconBase64(url):
  icon = favicon.get(url)[-1]
  icon_url = icon.url
  icon_format = icon.format
  response = requests.get(icon.url, stream=True)
  # Return the b64 encoded icon
  return "data:"+str(response.headers['Content-Type'])+";"+"base64,"+base64.b64encode(response.content).decode("utf-8")
  
while True:
  # Menu
  menu_selection = int(input("1. Create Folder\n2. Done\n> "))
  if menu_selection == 2: 
    break
  elif menu_selection == 1:
    folder_name = input("Please enter a folder name\n> ")
    formatted_links = ""
    # Ask for links
    while True:
      link = {}
      link_name = input("Enter a link name (blank to stop adding)\n> ")
      if link_name == "":
        break
      link["name"] = link_name
      link["url"] = input("Enter a link URL\n> ")
      # Try and get the b64 encoded site icon. If not use nothing (browser will cache icon if not present)
      try:
        link["icon"] = getIconBase64(link["url"])
      except: 
        link["icon"] = ""
      # Add link to existing lists
      formatted_links = formatted_links + '\n\t\t\t<DT><A HREF="{}" ADD_DATE="{}" ICON="{}">{}</A>'.format(link["url"], round(time.time()), link["icon"], link["name"])
    # Create folder and add to current folders
    folder_objects = folder_objects+'\n\t\t<DT><H3 ADD_DATE="{}" LAST_MODIFIED="{}">{}</H3>\n\t\t<DL><p>{}\n\t\t</DL><p>'.format(round(time.time()), round(time.time()), folder_name, formatted_links)
    
# Add folders to overall bookmarks object
bookmarks_object = '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n<TITLE>Bookmarks</TITLE>\n<H1>Bookmarks</H1><DL><p>\n\t<DT><H3 ADD_DATE="{}" LAST_MODIFIED="{}" PERSONAL_TOOLBAR_FOLDER="true">Bookmarks</H3>\n\t<DL><p>{}\n\t</DL><p>\n</DL><p>'.format(round(time.time()), round(time.time()), folder_objects)
  
# Write bookmarks to file
bookmarks_file = open("./bookmarks.html", "w")
bookmarks_file.writelines(bookmarks_object)