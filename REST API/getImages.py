import pandas as pd
import numpy as np

df=pd.read_csv('products.csv') 
my_products=np.array(df['Products'])

#for image display without requiring disk read and write
from io import BytesIO
my_bytes_io = BytesIO()
from PIL import Image


# import os
# from dotenv import load_dotenv
# load_dotenv('.env')

#You need developer key and cx to access the google api
__DEVELOPER_KEY__= "AIzaSyD9uE9oh_LtPzHN52U2AgzKLkD-svW19gg"
__CX__="77c3d0b83dd714d54"


#To search for google images
from google_images_search import GoogleImagesSearch   

# You need to get your own CX and Developer Key
#  https://pypi.org/project/Google-Images-Search/ visit this link for steps
gis = GoogleImagesSearch(__DEVELOPER_KEY__,__CX__) 

for product_name in my_products:
    _search_params = {
            'q': product_name,
            'num': 3,
            'fileType': 'jpg',
            'safe': 'safeUndefined', ##
            'imgType': 'imgTypeUndefined', ##
            'imgSize': 'imgSizeUndefined', ##
            'imgDominantColor': 'imgDominantColorUndefined', ##
            'imgColorType': 'imgColorTypeUndefined' ##
        }

    gis.search(search_params=_search_params)
    for image in gis.results():
        my_bytes_io.seek(0)
        
        image.copy_to(my_bytes_io)

        my_bytes_io.seek(0)
        temp_img= Image.open(my_bytes_io)
        temp_img.show()

        # Now we get other information too, like url,etc, check the docs for full info
        # print(image.url)
        
        #or I can save the image as well 
        # image.referrer_url  # image referrer url (so77c3d0b83dd714d54urce) 
    
        # image.download('/path/')  # download image
        # image.resize(500, 500)  # resize downloaded image

        # image.path  # downloaded local file path




# getting api key and cx 

# : skillful-cider-375310.

# api key : AIzaSyD9uE9oh_LtPzHN52U2AgzKLkD-svW19gg 

# <script async src="https://cse.google.com/cse.js?cx=77c3d0b83dd714d54">
# </script>
# <div class="gcse-search"></div>

