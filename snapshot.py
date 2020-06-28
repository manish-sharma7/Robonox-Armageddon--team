import picamera
camera = picamera.PiCamera()

def snapshot():
    """
    Returns: void
    function: stores an image under 'tmp.png'
    """
    camera.capture("tmp.png")