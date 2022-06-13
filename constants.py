CAPTURE_SOURCE = 0

# Windows settings: 640x480@10/15/30, 1280x720@10/15/30, 1920x1080@10/15/30
# Raspbian settings: 1920x1088@30, 1280x720@60, more here https://picamera.readthedocs.io/en/release-1.13/fov.html

class SETTING:
    resolution = (640, 480)
    croppedResolution = (640, 480)
    frameRate = 30
    duration = 5

class OS:
    windows = 'Windows'
    raspbian = 'Linux'

CAPTURE_DELAY = int(1000 / SETTING.frameRate * 0.8)  # multiplied by a correction factor
CROP_PADDING = ((SETTING.resolution[0] - SETTING.croppedResolution[0]) // 2, (SETTING.resolution[1] - SETTING.croppedResolution[1]) // 2)
