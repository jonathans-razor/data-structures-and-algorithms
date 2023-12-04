import pip

try:
  import pyperclip
except ImportError:
  pip.main(['install', 'pyperclip'])
  import pyperclip

# Get the contents of the clipboard
clipboard_contents = pyperclip.paste()

# Open a file for writing
with open("c:\\a\\j1.txt", "w") as f:
  # Write the contents of the clipboard to the file
  f.write(clipboard_contents)