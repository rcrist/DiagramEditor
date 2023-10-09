# Diagram Editor

![Diagram Editor Screen Shot](screen_captures\Screenshot 2023-10-09 052605.jpg)

Python diagramming program written for educational purposes. The graphics library is CustomTkinter by 
Tom Shimansky(https://customtkinter.tomschimansky.com/) which provides a modern user interface with light and 
dark modes.

Required libraries:
 -  pip install customtkinter
 -  python.exe -m pip install --upgrade pip
 -  pip install ctkcolorpicker
 -  pip install tkinter-tooltip
 -  pip install pyInstaller - Create .exe file

Features:
 - Object-oriented design approach
 - Modular design with classes stored in module files
 - Shape library includes rectangle, oval, triangle, line, text, and image
 - Shape modifications for fill color, border (outline) color, and border width
 - Transformations including move, rotate, and resize
 - Shape selection, 90 deg rotation with 'r' and 'e' keys
 - Selected shape displays connectors where lines can connect to the shape (snap to shap)
 - Lines resize when connected shape is moved
 - Background grid with adjustable grid spacing and on/off control
 - Snap to grid for initial shape drawing and subsequent move/resize operations
 - Snap menus to change the snap size except rotation which is fixed at 90 deg
 - Modify text with mouse right click
 - Modify images with mouse right click
 - Save and open diagrams in json file format
 - Delete selected shape using Delete key
