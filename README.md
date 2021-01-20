# dwimgs

`dwimgs` is a simple Python command line utility to batch download images using a simple text file.

## **INSTALLATION**

`dwimgs` is available on `PyPI`, so you can simply install it using the following command:

    pip install dwimgs

This will install all the required packages and add the `dwimgs` utility to your path allowing you to start using it immediately. To ensure that it was installed successfully, run the following command:

    dwimgs --version

If the package was installed successfully, you should get an output that looks like this:

> dwimgs 1.0 © 2021 by Abdelrahman Said

## **USAGE**

To find out how to use the utility, you can simply run:

    dwimgs -h

OR

    dwimgs --help

This will give you the following output:

    usage: dwimgs [-h] [-v] [--version] urls_file dest_dir

    positional arguments:
      urls_file      A text file that has image URLs on separate lines
      dest_dir       The destination directory where the images will be saved. The
                     directory will be created if it doesn't exist.

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  increase the verbosity of the terminal output
      --version      show program's version number and exit

As you can see, `dwimgs` takes two simple ***required*** arguments:

1) A text file with URLs to images on the internet, with each URL placed on a separate line.
2) A folder on your system where the downloaded images will be saved.

So, if you have a file called `links.txt` with valid URLs to images and you want to save them in a folder called `Pictures`, all you need to do is run the following command:

    dwimgs links.txt Pictures

This will look for the `links.txt` file and the `Pictures` folder in the current directory. If it cannot find the file, then it will output an error message that looks like this:

    ERROR: The URL files provided doesn't exist [/home/abdelrahman/links.txt]

However, if the `Pictures` folder doesn't exist, it will simply create it.

Please note, that the order is important. You have to specify the file first then the folder.

## **FILE NAMES**

`dwimgs` tries to extract the image's file name from the URL. If it fails, it just generates a simple name and saves the image.

Additionally, since it is common to get two different images with the same name, `dwimgs` will check before downloading an image to make sure that there aren't any other images with the same name. If it finds one, it will just add the date and time of download to the end of the file name to make it unique. This ensure that an image you have previously downloaded won't get overwritten with another image that just happens to have the same name.

## **CHECKING THE DOWNLOADS**

Since there is no guarantee that all the links you provide will work, `dwimgs` stores the results of the download process in a file called `result.json` that is saved next to the downloaded images in the folder you specified as a destination.

The file contents will look like this:

    {
        "URLs processed": 2,
        "Downloads succeeded": 1,
        "Downloads failed": 1,
        "Failed downloads": [
            "https://cache.marriott.com/marriottassets/marriott/NYCSW/nycsw-exterior-9397-hor-feat.jpg"
        ],
        "Successful downloads": [
            "https://cdn.cnn.com/cnnnext/dam/assets/171008203711-times-square.jpg"
        ]
    }

As you can see, it includes the number of the URLs it processed, how many were downloaded successfully and how many failed. More importantly, it includes two lists, one that includes the links for the failed downloads and for the successful downloads. This allows you to open the links for the failed ones and either figure out why they failed or just download them manually.

___

## DEVELOPER DOCUMENTATION

If you wish to download the source code and start experimenting with it, here is what you need to do.

1) Download the source code and navigate to its directory

        git clone https://github.com/amsaid1989/bulk-download-images.git
        cd bulk-download-images

2) Using your Python of choice, create a virtual environment in a separate folder (usually called `env`, but you can call it whatever you want)

        python -m venv env
    
3) Activate the virtual environment. On `Linux` and `MacOS`, do the following if you are using `bash` as your shell:

        source env/bin/activate

4) On `Windows`, you will need to do the following if you are using `Command Prompt`:

        env/Scripts/activate.bat

5) Install the required packages

        pip install -r requirements.txt

That is it. Now, you shoud be able to run `dwimgs` and modify the code as you like. To make sure everything is working properly, run the following command:

    python src/dwimgs/run.py --version

If everything is working properly, you should get the following output:

> dwimgs 1.0 © 2021 by Abdelrahman Said

