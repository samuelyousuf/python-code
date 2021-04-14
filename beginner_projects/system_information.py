'''This script provides your system's Python version, hardware platform, and OS name.'''
import platform

# Get the Python version innstalled on your system.
pythonInfo = platform.python_version()
print("Python version is {}.".format(pythonInfo))

# Get your system's underlying hardware platform.
sysPlatform = platform.platform()
print("Hardware platform information is {}.".format(sysPlatform))

# Get your OS name.
systemOS = platform.system()
print("Operating system name is {}.".format(systemOS))
