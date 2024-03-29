# DaFbc

DaFbc is a background image conversion tool for Mo Young / Da Fit binary files.

With that tool you can convert a background image in binary format to your MoYoung v2 watch.

**NOTE: This tool is in alpha stage, so expect some bugs.**

## Supported OS

The tool was developed for Linux, however it may work on other OS if the dependencies are fulfilled.

## Dependencies

- Python 3.x
- [Pillow](https://github.com/python-pillow/Pillow)
- [numpy](https://github.com/numpy/numpy)

Install them using your preferred method.

In Arch Linux for example you can install through repositories:

    # pacman -S python-pillow python-numpy

## Usage

#### How to run (Linux)

First the dependencies must be fulfilled, check them above.

In a command line, give the file execution permissions:

    $ chmod +x DaFbc.py

Then you can run it like that:

    $ ./DaFbc.py ./myimage.jpg ./myimage.bin

## Supported watches

Da Fit watches with 240x296 resolution should be supported.

Other watch resolutions may work with some code changes.