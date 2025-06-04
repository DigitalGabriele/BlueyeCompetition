import cv2
from cv2 import aruco
import os
import time
import math
import blueye.protocol as bp
from blueye.sdk import Drone


def detect_specific_aruco_tags(
    gst_pipeline: str,
    dict_name: int,
    tag_ids: tuple = 
) -> None:
    """
    Continuously read frames from a GStreamer-based RTSP video stream
    and detect ArUco tags in the provided `tag_ids`.

    Args:
      gst_pipeline: Predefined GStreamer pipeline string for RTSP input
      dict_name:    Predefined ArUco dictionary (e.g. aruco.DICT_4X4_50)
      tag_ids:      Tuple of tag IDs to look for (default: 48 and 50)

    Returns:
      None
    """

    pass


if __name__ == "__main__":
	gst_pipeline = 'rtspsrc latency=0 location=rtsp://192.168.1.101:8554/test ! decodebin ! videoconvert ! appsink'
	dict_name = aruco.DICT_4X4_50
  tag_ids = (48, 50)
	detect_specific_aruco_tags(gst_pipeline, dict_name, tag_ids)