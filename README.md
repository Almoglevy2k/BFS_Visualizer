# BFS Visualization
This project visualizes the **Breadth-First Search (BFS)** algorithm on a graph with interactive animations using `matplotlib` and `networkx`. The graph is visualized dynamically, showing the BFS traversal, node colors, and depths in real time. Users can choose between automatic or manual control over the visualization.

## About This Project
This project was developed as a personal initiative to explore and visualize the **Breadth-First Search (BFS)** algorithm in an interactive and educational way. It is not part of any mandatory coursework but rather a side project created out of interest in algorithm visualization and dynamic graph representation. The goal was to make BFS traversal both intuitive and visually engaging, catering to students, enthusiasts, and professionals alike who wish to see the algorithm in action.


## Features
- **Interactive Visualization**: The graph updates in real-time as BFS is executed, showing the current node, visited nodes, and newly discovered nodes.
- **Node Depths**: Displays the depth of each node during traversal.
- **Graph with Multiple Depth Levels**: The graph is created with nodes that go to depth 4, ensuring more complex and interesting BFS visualizations.
- **Manual/Automatic Modes**: The user can either step through the BFS iteration manually or let it play automatically with adjustable speed.
- **Customizable Speed**: In automatic mode, you can control the speed of the animation to match your preferences.

## Requirements

Before running the project, ensure that you have the following dependencies installed:

- Python 3.6 or higher
- `matplotlib`
- `networkx`

You can install the required packages using `pip`:

## How to Run

### Step 1: Install Dependencies
Ensure you have the required dependencies installed. Run:

```bash
pip install matplotlib networkx
```
##Automatic Mode
-**In automatic mode, the visualization runs automatically, with a pause between each step. You can adjust the speed using the --speed argument.
-**--speed (optional): Pause duration between iterations. Default is 3.0 seconds. Recommended range: 0.5 to 5.0 seconds.
```bash
python BFS.py auto --speed 2.0
or
python BFS.py auto
```
##Manual Mode
-**In manual mode, you control the BFS iterations manually by pressing any key in the graph window.

To run in manual mode:
```bash
python BFS.py manual
```

