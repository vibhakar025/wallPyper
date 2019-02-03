import requests,ctypes,urllib,os
from PIL import Image
from io import BytesIO

def get_url():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    w,h=user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
    screencode=str(w)+'x'+str(h)
    url = r'https://source.unsplash.com/random/'+screencode
    return url

def set_wall():
    imgsrc=get_url()
    urllib.request.urlretrieve(imgsrc, 'wall.jpg')
    path=os.path.abspath('wall.jpg')
    ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
    

set_wall()
