# Image Matching Python Script

## How to use:
* Open the "image_matching.py" file in a text editor
* Input the desired URL(s) in the "web_urls" list
* Input the desired search tag(s) in the "search_tags" list
* Run the script and all matching image URL(s) will be displayed

## How it works:
1. The script goes through each of the URLs and extracts the HTML code
2. From the extracted HTML code, only the img tags are extracted and kept in a list
3. From the img tags, the "src" and "alt" attribute are extracted individually
4. Each of the search tags are matched with both the "src" and "alt" attribute, if there is a match then a flag is set to true
5. Finally, if the flag is true, that particular img src is printed which shows the URL of that image
