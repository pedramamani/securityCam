CAPTURE_SOURCE = 0

# Windows settings: 640x480@10/15/30, 1280x720@10/15/30, 1920x1080@10/15/30
# Raspbian settings: 1920x1088@30, 1280x720@60, more here https://picamera.readthedocs.io/en/release-1.13/fov.html

class SETTING:
    frameRate = 30
    duration = 5
    resolution = (640, 480)
    cropResolution = (300, 300)
    cropCenter = (356, 254)
    cropPadding = ((resolution[0] - cropResolution[0]) // 2, (resolution[1] - cropResolution[1]) // 2)
    cropStart = (cropCenter[0] - cropPadding[0], cropCenter[1] - cropPadding[1])
    cropEnd = (cropCenter[0] + cropPadding[0], cropCenter[1] + cropPadding[1])


class OS:
    windows = 'Windows'
    raspbian = 'Linux'

CAPTURE_DELAY = int(1000 / SETTING.frameRate * 0.8)  # multiplied by a correction factor
