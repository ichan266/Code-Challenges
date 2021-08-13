import webbrowser
import sys
import pyperclip

sys.argv

# Check if command line argument are passed
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
