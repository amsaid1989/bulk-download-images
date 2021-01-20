# Copyright 2021 Abdelrahman Said
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the
# following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

"""Module that implements the download_image function which takes
a URL and a valid download directory and save the image file to
that directory.

Module: image_downloader
Author: Abdelrahman Said
"""

import os
from datetime import datetime
import requests


unknown_image_counter = 1

IMG_FORMATS = ['jpg', 'jpeg', 'png', 'webp']


def get_filename(url):
    """Extracts an image filename from a URL

    Arguments:
        url : str
            The URL to the image file
    
    Returns:
        filename : str
            The clean filename or an empty string if it couldn't extract
            a name from the provided URL
    """
    filename = ''

    # Check to see if one of the valid image extensions exist in the URL.
    # If it does, split the URL at the '/' character and remove any
    # characters after the extension
    for ext in IMG_FORMATS:
        if ext in url:
            index = url.index(ext) + len(ext)
            clean_name = url[:index]
            filename = clean_name.split('/')[-1]
    
    return filename


def download_image(url, download_dir):
    """Takes a URL and downloads the image to the specified download
    directory.

    Arguments:
        url : str
            The URL to the image file
        download_dir : str
            The path to the directory where the downloaded files will
            be saved
    
    Returns:
        True if it managed to download the image, otherwise False
    """
    filename = get_filename(url)

    global unknown_image_counter

    # If the get_filename function returned an empty string, then
    # construct a default filename
    if not filename:
        # Get the date and time signature to create a unique file name
        now = datetime.strftime(datetime.now(), '%y%m%d_%H%M%S')
        
        filename = f'image_{unknown_image_counter:03}_{now}.jpg'

        unknown_image_counter += 1
    
    # Create the path to the image file
    filepath = os.path.join(download_dir, filename)

    # Ensure a unique filepath
    if os.path.exists(filepath):
        # Get the date and time signature to create a unique file name
        now = datetime.strftime(datetime.now(), '%y%m%d_%H%M%S')

        # Split the extension and add the datetime signature to the file name
        path = list(os.path.splitext(filepath))
        path[0] += f'_{now}'

        # Recreate the file name
        filepath = ''.join(path)

    r = requests.get(url)
        
    # Make sure that the request was valid and that the content returned
    # is an image file
    if r.ok and 'image' in r.headers['Content-Type']:
        with open(filepath, 'wb') as image_file:
            image_file.write(r.content)
        
        r.close()

        return True
    
    return False


__all__ = ['download_image']
