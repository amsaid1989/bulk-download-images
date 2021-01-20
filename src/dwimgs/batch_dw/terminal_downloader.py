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

"""This module implements the terminal utility dwimgs, which takes a file
that contains URLs to image files and a directory and then downloads each
image to the specified directory.

Module: download_images
Author: Abdelrahman Said
"""

import os
import argparse
import json
import requests
from datetime import datetime
from utils import ansi_escape_codes as esc
from utils import image_downloader as img_dl
from utils import package_info

# CONSTANTS
PROGRAM_VERSION_MSG = f'%(prog)s {package_info.version} \u00a9 ' \
                      f'{datetime.today().year} by {package_info.author}'

# Create the parser
parser = argparse.ArgumentParser(prog=package_info.name)

# Add all the arguments
parser.add_argument('urls_file',
                    help='A text file that has image URLs on separate lines')
parser.add_argument('dest_dir',
                    help="The destination directory where the images will be saved. "\
                         "The directory will be created if it doesn't exist.")
parser.add_argument('-v', '--verbose', action='store_true',
                    help='increase the verbosity of the terminal output')
parser.add_argument('--version', action='version', version=PROGRAM_VERSION_MSG)


def download_images():
    """Runs the command line utility ensuring that all positional arguments
    are satisified and then it downloads all the images to the specified
    destination directory.

    Lastly, it creates a JSON file in the specified destination directory
    showing the images that were downloaded successfully and the ones that
    failed to download.
    """

    def print_error_message(msg, origin):
        """Prints a formatted error message to stdout
        
        Arguments:
            msg : str
                The message that will be printed to stdout
            origin : str
                The name of the object that caused the error
        """

        print(f'{esc.RED}{esc.BOLD}{msg}{esc.RESET}',
              f'[{esc.ITALIC}{origin}{esc.RESET}]')
                

    # Parse the command line arguments
    args = parser.parse_args()

    # Lists to store the files that succeeded and the files that failed
    success = []
    failure = []

    # Counter for how many URLs were processed
    url_count = 0

    try:
        # Get the arguments
        urls_file = os.path.abspath(args.urls_file)
        download_dir = os.path.abspath(args.dest_dir)

        # Check that the specified directory exists and that it is valid.
        # If it exists but it is not a directory, raise an error.
        if os.path.exists(download_dir) and not os.path.isdir(download_dir):
            raise NotADirectoryError
        # If it doesn't exist, create it
        elif not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # Go through the URLs file and try to download the image. If it
        # downloads successfully, add it to the list of the files that
        # succeeded. Otherwise, add it to the list of the failed files.
        with open(urls_file, 'r') as urls:
            for url in urls.readlines():
                # Strip the URL of the newline character
                url = url.strip()

                if args.verbose:
                    print(f'{esc.GREEN}Downloading{esc.RESET}',
                          f'{esc.ITALIC}{url}{esc.RESET}')

                # Attempt downloading the image
                if img_dl.download_image(url, download_dir):
                    success.append(url)
                    print(f'{esc.GREEN}{esc.BOLD}Download successful{esc.RESET}\n')
                else:
                    failure.append(url)
                    print(f'{esc.RED}{esc.BOLD}Download failed{esc.RESET}\n')
                
                # Increment the URL counter
                url_count += 1

        # Construct the json dictionary that will be passed to the log file
        json_object = {
            'URLs processed': url_count,
            'Downloads succeeded': len(success),
            'Downloads failed': len(failure),
            'Failed downloads': failure,
            'Successful downloads': success
        }

        log_file = os.path.join(download_dir, 'result.json')

        # Write the dictionary to the json log file
        with open(log_file, 'w+') as result:
            json.dump(json_object, result, indent=4)
    except NotADirectoryError:
        print_error_message('ERROR: Invalid destination directory',
                            download_dir)
    except FileNotFoundError:
        print_error_message("ERROR: The URL files provided doesn't exist",
                            urls_file)
    except PermissionError:
        print_error_message("ERROR: You can't write to this directory",
                            download_dir)
    except requests.exceptions.MissingSchema:
        print_error_message('ERROR: Invalid URLs provided', urls_file)
