# BFS Visualization

This project visualizes the **Breadth-First Search (BFS)** algorithm on a graph with interactive animations using `matplotlib` and `networkx`. The graph is visualized dynamically, showing the BFS traversal, node colors, and depths in real time. Users can choose between automatic or manual control over the visualization.

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

```bash
pip install matplotlib networkx

## How to Run

### Automatic Mode
In **automatic mode**, the BFS visualization will run automatically with a default pause between each step. You can adjust the speed using the `--speed` argument.

To run in **automatic mode**:

```bash
python BFS.py auto --speed 2.0
--speed (optional): Defines the pause between iterations (default is 3.0 seconds). Recommended range is between 0.5 and 5.0 seconds.

Manual Mode
In manual mode, you will step through each iteration manually by pressing any key in the graph window.
python BFS.py manual

