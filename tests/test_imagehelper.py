from imageworker import __version__
from imageworker import put_qiniu, url_to_array,file_to_array
import numpy as np
def test_version():
    assert __version__ == '0.1.0'

def test_image():
    f = file_to_array("tests/R90ca7122a356d0ae6eaba3baa5042db5.jpeg")
    print(f)


def test_url_to_array():
    url = "https://n.sinaimg.cn/spider2021326/106/w1024h682/20210326/5927-kmvwsvy1040641.jpg"
    np = url_to_array(url)
    print(np)
