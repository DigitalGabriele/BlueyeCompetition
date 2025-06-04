import time
import math
from blueye.sdk import Drone
import blueye.protocol as bp

def toggle_external_light(
    intensity: float = 1.0,
    on_time: float = 5.0
) -> None:
    """
    Args:
      intensity: Brightness level (0.0 = off … 1.0 = full)
      on_time:   Seconds to keep the light on

    Returns:
      None
    """

    pass


# Example usage
if __name__ == "__main__":
    toggle_external_light()