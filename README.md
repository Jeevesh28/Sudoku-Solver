# Sudoku-Solver :1234:
Sudoku is a logic based combinatorial number placement puzzle. The puzzle’s goal is to fill a 9x9 grid such that each of the nine blocks (3x3 grids) has to contain all the digits 1-9 and each number can only appear once in a row, column or box. [Sudoku Rules](https://www.sudokukingdom.com/rules.php)

This program serves as a way to calculate the solution to any 9x9 sudoku puzzle via webcam. It identifies the puzzle through the webcam, processes it using **OpenCV**, runs against a neural network trained on **MNIST digits dataset** to predict the digits, and runs a **backtracking algorithm** to determine the solution.

## Instructions:🎮

**File:** mainTestWebcam.py

**Purpose:**
<ol>
<li> This file is used to get answer from sudoku image capture through the webcam. First, it detects the sudoku grid and when it shows 'Detected :)' symbol Press 'C' to capture</li>
<li> After capturing it process the image and detect number written on the grid. For this it uses pre-trained model from model folder 'Models/digitRecognisor.h5' present at project directory (or you can train custom one using 'Models/kerasModel.h5')</li>
<li> After that it uses Backtracking Algorithm to predict the grid from 'backtrackingAlgo.py' file</li>
</ol>
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**File:** backtrackingAlgo.py

**Purpose:** 

<ol>
<li> Contains main Backtracking Algorithm 
</ol>

## Screenshots: 📷

| *Identified Digits* |
|:--:| 
| <img width="1000" height="350" src="https://github.com/Jeevesh28/Sudoku-Solver/blob/main/Images/savedDigits.png">| 




Input Sudoku      |  Output Sudoku
:-------------------------:|:-------------------------:
<img width="1000" height="300" src="https://github.com/Jeevesh28/Sudoku-Solver/blob/main/Images/Input.png"> |  <img width="1000" height="300" src="https://github.com/Jeevesh28/Sudoku-Solver/blob/main/Images/Output.png">



