# Setup

pyrealsense2 does not support Python 3.8 so use Python 3.7.

## Install Python 3.7

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7
```

The Python executable is `python3.7`. If you want you can append `alias python=python3.7` to ~/.bashrc if you want.

## Install pyrealsense2

```
python3.7 -m pip install pyrealsense --user
```
