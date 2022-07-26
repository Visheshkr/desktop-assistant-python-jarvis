import webbrowser
def open():
    try:
        webbrowser.open('https://codewithharry.com/videos/python-tutorials-for-absolute-beginners-120')
        webbrowser.open('http://localhost/phpmyadmin/index.php?route=/database/structure&server=1&db=codingthunder')
        webbrowser.open('https://www.youtube.com/c/CodeWithHarry')   
        webbrowser.open('https://www.youtube.com/playlist?list=PLUcsbZa0qzu3yNzzAxgvSgRobdUUJvz7p')      

    except Exception as e:
        print(e)
        print("Sorry unable to open the link\n")
open()        