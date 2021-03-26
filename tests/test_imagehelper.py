from imageworker import __version__
from imageworker import put_qiniu, url_to_array,file_to_array
from imageworker import url_to_file
from imageworker import file_to_file
import numpy as np
import time


def test_version():
    assert __version__ == '0.1.11'

def test_image():
    f = file_to_array("tests/R90ca7122a356d0ae6eaba3baa5042db5.jpeg")


def test_url_to_array():
    url = "https://pic.igengmei.com/ff68d821451da2906a3a18bc9ff8b1c6.png?e=1616765928&token=UPCOYIJkZOMcdd9FDzpBqYjzWUh55fBpVi3AhWpL:L0baCqx0R8uUaG38RWzOwV4zfBA="
    start = time.time()
    np = url_to_array(url)
    print(time.time() - start)

def test_url_to_file():
    url_to_file("https://pic.igengmei.com/bd121b884a23d9b28325bd3d3d0b4d4f.png?e=1616764457&token=UPCOYIJkZOMcdd9FDzpBqYjzWUh55fBpVi3AhWpL:Ekn8iXTqcLWHa6uLbDt58YUv9cE=")

def test_file_to_file():
    file_to_file("tests/1.png","r.png")
