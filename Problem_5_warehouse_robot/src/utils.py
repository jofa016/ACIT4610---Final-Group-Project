import gymnasium as gym


def make_env(
    map_name: str = "4x4",
    slippery: bool = True,
    max_steps: int = 200,
    render_mode: str | None = None,
):
    """
    Create a FrozenLake-v1 environment with consistent settings.

    Parameters
    ----------
    map_name : {"4x4", "8x8"}
        Grid size.
    slippery : bool
        If True, stochastic transitions.
    max_steps : int
        Max steps before episode truncation.
    render_mode : {"rgb_array", "ansi", None}
        Rendering mode. Use None for training, "rgb_array" for visualization.

    Returns
    -------
    env : gym.Env
        Configured FrozenLake environment.
    """
    env = gym.make(
        "FrozenLake-v1",
        map_name=map_name,
        is_slippery=slippery,
        render_mode=render_mode,
        max_episode_steps=max_steps,
    )
    return env


def epsilon_step_decay(
    episode: int,
    step_size: int,
    epsilon_initial: float,
    epsilon_min: float,
    decay_factor: float = 0.5,
) -> float:
    """
    Step-wise epsilon decay.

    Every `step_size` episodes, epsilon is multiplied by `decay_factor`
    until it reaches `epsilon_min`.

    eps_k = max(epsilon_min, epsilon_initial * decay_factor^k),
    where k = floor(episode / step_size).
    """
    steps = episode // step_size
    epsilon = epsilon_initial * (decay_factor ** steps)
    return max(epsilon_min, epsilon)
