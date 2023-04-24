from setuptools import setup, find_packages

# More packages maybe required to be installed but since we are using
# yolov7 in python-model a lot of packages like cv2, numpy are already installed
setup(
    name="yolov7",
    version="1.0",
    packages=find_packages(),
    install_requires=["pandas", "seaborn"],
)
