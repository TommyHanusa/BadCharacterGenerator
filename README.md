# BadCharacterGenerator
0. This is a small project to understand the basics of Tkinter and Python UIs. The aim was to make a character portrait generator that could be built out as a stand alone exe. BadCHaracterGenerator.py is the script for the application.

1. It is important that you have pillow installed for this script to run.

  http://pillow.readthedocs.org/en/3.0.x/installation.html
  
  $ pip install Pillow 

2. Running the script or the shortcut launches the GUI for the character portrait generator
  - random will make a random portrait
  - saving will pop up a save dialog to save your generated character portrait
  - The script itself could maybe use some cleanup (I should remove some print statements)
  - you can add pngs to the folders (head,eyes,nose,mouth,hair) and they should show up if you run the script (but not the exe). Keep in mind there are two sets of image files, one is for testing with the script and the other is for the exe. This is based on how the distrubutable exe is built with PyInstaller. (and for those Familiar with PyInstaller I have a txt copy of the .spec thrown in there incase you/I overwrite it when I'm making changes)

3. This project also serves as a case study for why you should get a decent artist and UI designer when working on projects.
