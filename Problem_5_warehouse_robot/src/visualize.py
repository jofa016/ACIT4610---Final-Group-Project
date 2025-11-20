import argparse
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
from time import sleep

from Problem_5_warehouse_robot.src.utils import make_env


def run_visualization(qtable_path, map_name="4x4", delay=0.4):

    # Load Q-table
    Q = np.load(qtable_path)

    # Create environment with proper render_mode
    env = make_env(
        map_name=map_name,
        slippery=True,
        max_steps=500,
        render_mode="rgb_array"     # REQUIRED FOR VISUALIZATION
    )

    state, info = env.reset()
    done = False

    print(f"Running visualization for {map_name} map...")

    while not done:

        # Choose greedy action
        action = int(np.argmax(Q[state]))

        # Step environment
        next_state, reward, done, truncated, info = env.step(action)
        done = done or truncated

        # Render current frame
        frame = env.render()

        if frame is None:
            print("ERROR: env.render() returned None. Check render_mode='rgb_array'.")
            break

        plt.imshow(frame)
        plt.axis("off")
        clear_output(wait=True)
        plt.pause(delay)

        state = next_state

    clear_output(wait=False)
    print("Visualization finished.")
    print("Final reward:", reward)


# CLI support
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Visualize FrozenLake agent")

    parser.add_argument("--qtable", required=True, type=str)
    parser.add_argument("--map", default="4x4", type=str)
    parser.add_argument("--delay", default=0.4, type=float)

    args = parser.parse_args()

    run_visualization(args.qtable, args.map, args.delay)
