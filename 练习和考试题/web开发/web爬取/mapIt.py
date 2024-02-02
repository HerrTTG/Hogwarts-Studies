#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = " ".join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open("https://map.baidu.com/search/" + address + "/@13228398.225,3724267.59,19z?querytype=s&da_src=shareurl&wd="+address)
