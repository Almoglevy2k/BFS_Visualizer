import networkx as nx
import matplotlib.pyplot as plt
import argparse
import sys


def BFS(graph, start):
    # BFS implementation
    visited = [False] * len(graph)
    queue = [start]
    depths_list = [-1] * len(graph)  # Initialize all depths as -1
    depths_list[start] = 0  # Start node is at depth 0
    visited[start] = True  # Mark start node as visited

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                depths_list[neighbor] = depths_list[node] + 1  # Depth is parent's depth + 1
                queue.append(neighbor)

    return depths_list

def plot_graph(G, pos, depths_list, current_node, new_neighbors, visited, iteration, mode, speed, ax):
    # Determine colors for nodes
    node_colors = []
    for n in G.nodes:
        if n == current_node:
            node_colors.append("gold")  # Current node is gold
        elif n in new_neighbors:
            node_colors.append("lightgreen")  # Newly discovered neighbors are light green
        elif visited[n]:
            node_colors.append("lightblue")  # Visited nodes are light blue
        else:
            node_colors.append("lightcoral")  # Unvisited nodes are light red

    # Increase k for more space between nodes and larger arrows
    ax.clear()  # Clear the axes without closing the figure
    nx.draw(
        G, pos, with_labels=True,
        labels={n: f"q{n+1}\nDepth: {depths_list[n]}" if depths_list[n] != -1 else f"q{n+1}" for n in G.nodes},
        node_color=node_colors, font_size=8, node_size=1800, ax=ax, arrowsize=10, font_weight="normal", 
    )
    ax.set_title(f"BFS Iteration: {iteration}", fontsize=10)  # Title font size is also adjusted

    # Add a legend below the plot in a fixed box
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', label='Current Node', markersize=10, markerfacecolor='gold'),
        plt.Line2D([0], [0], marker='o', color='w', label='New Neighbors', markersize=10, markerfacecolor='lightgreen'),
        plt.Line2D([0], [0], marker='o', color='w', label='Visited Nodes', markersize=10, markerfacecolor='lightblue'),
        plt.Line2D([0], [0], marker='o', color='w', label='Unvisited Nodes', markersize=10, markerfacecolor='lightcoral')
    ]
    ax.legend(
        handles=legend_elements,
        loc='lower center',  # Place legend below the graph
        bbox_to_anchor=(0.5, -0.25),  # Adjust position to stay fixed
        frameon=True,  # Add a frame around the legend
        title="Legend",
        ncol=4  # Arrange legend items in a single row
    )

    plt.tight_layout()  # Adjust spacing to prevent overlap
    plt.draw()

    # Handle the mode for advancing
    if mode == "auto":  # Automatic mode
        plt.pause(speed)  # Use the speed value for the pause
    elif mode == "manual":  # Manual mode
        print("Press any key in the graph window to proceed...")
        plt.waitforbuttonpress()  # Wait for a keypress or mouse click in the plot

def prep_to_graph(graph):
    # Create a graph object
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Prepare layout and visualization setup
    pos = nx.spring_layout(G)  # Layout for graph visualization
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots(figsize=(10, 7))  # Set default figure size for better layout

    return G, pos, fig, ax

def BFS_with_visualization(graph, start, mode, speed):
    # BFS implementation with visualization
    visited = [False] * len(graph)
    queue = [start]
    depths_list = [-1] * len(graph)  # Initialize all depths as -1
    depths_list[start] = 0  # Start node is at depth 0
    visited[start] = True  # Mark start node as visited

    # Prepare the graph for visualization
    G, pos, fig, ax = prep_to_graph(graph)

    # BFS Loop
    iteration = 0
    while queue:
        iteration += 1
        current_node = queue.pop(0)
        neighbors = graph[current_node]

        # Update neighbors' depths and mark as visited
        new_neighbors = []  # Track neighbors to color green
        for neighbor in neighbors:
            if not visited[neighbor]:
                visited[neighbor] = True
                depths_list[neighbor] = depths_list[current_node] + 1
                queue.append(neighbor)
                new_neighbors.append(neighbor)

        # Call the plotting function
        plot_graph(G, pos, depths_list, current_node, new_neighbors, visited, iteration, mode, speed, ax)

        # Check if the window is closed (to avoid further errors and infinite pop-ups)
        if not plt.fignum_exists(fig.number):
            print("Graph window closed, stopping visualization.")
            break

    # Call the final graph rendering function
    end_graphing(G, pos, visited, depths_list, ax)

    return depths_list

def end_graphing(G, pos, visited, depths_list, ax):
    # Reset all nodes to their final colors
    final_colors = ["lightblue" if visited[n] else "lightcoral" for n in G.nodes]
    ax.clear()
    nx.draw(
        G, pos, with_labels=True,
        labels={n: f"q{n+1}\nDepth: {depths_list[n]}" if depths_list[n] != -1 else f"q{n+1}" for n in G.nodes},
        node_color=final_colors, font_weight="bold", node_size=1800, ax=ax, font_size=8  # Adjusted font size for labels
    )
    ax.set_title("Final BFS State", fontsize=10)  # Title font size is also adjusted

    # Add the legend below the plot in a fixed box
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', label='Current Node', markersize=10, markerfacecolor='gold'),
        plt.Line2D([0], [0], marker='o', color='w', label='New Neighbors', markersize=10, markerfacecolor='lightgreen'),
        plt.Line2D([0], [0], marker='o', color='w', label='Visited Nodes', markersize=10, markerfacecolor='lightblue'),
        plt.Line2D([0], [0], marker='o', color='w', label='Unvisited Nodes', markersize=10, markerfacecolor='lightcoral')
    ]
    ax.legend(
        handles=legend_elements,
        loc='lower center',  # Place legend below the graph
        bbox_to_anchor=(0.5, -0.25),  # Adjust position to stay fixed
        frameon=True,  # Add a frame around the legend
        title="Legend",
        ncol=4  # Arrange legend items in a single row
    )

    # Turn off interactive mode and finalize the plot
    plt.ioff()
    plt.show()

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="BFS Visualization",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "mode",
        type=str,
        choices=["auto", "manual"],
        help="Mode: 'auto' for automatic playback, 'manual' for step-by-step."
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=3.0,
        help=(
            "Pause duration between iterations in 'auto' mode (recommended range: 0.5 to 5.0).\n"
            "Default is 3.0 seconds."
        )
    )

    # If no arguments are provided, show the help message
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()

    # Test adjacency list
    graph = {
        0: [1, 2, 3],
        1: [0, 4, 5],
        2: [0, 6, 7],
        3: [0, 8],
        4: [1, 9, 10],
        5: [1, 11, 12],
        6: [2, 13],
        7: [2, 14],
        8: [3],
        9: [4],
        10: [4],
        11: [5],
        12: [5],
        13: [6],
        14: [7],
    }
    # Perform BFS
    start_node = 0
    BFS_with_visualization(graph, start_node, args.mode, args.speed)

if __name__ == "__main__":
    main()
