import time
import math
from blueye.sdk import Drone
import blueye.protocol as bp

def follow_square_path(
    side_length: float = 2.0,
    forward_speed: float = 0.3,
    yaw_speed: float = 0.3,
    depth: float = 1.5,
    depth_tolerance: float = 0.1,
    heading_tolerance: float = 5.0
) -> None:
    """
    Args:
      side_length:      Length (m) of each side of the square
      forward_speed:    Surge setpoint (0–1) for forward motion
      yaw_speed:        Yaw setpoint (0–1) for rotations
      depth:            Target depth (m) to dive before moving
      depth_tolerance:  Acceptable depth error (m)
      heading_tolerance: Acceptable heading error (°)

    Returns:
      None
    """

    pass

# Example usage
if __name__ == "__main__":
    follow_square_path()