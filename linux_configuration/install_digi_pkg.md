When attempting to install the digi-xbee package with pip, error is returned.

Solution adopted (no safer):

To bypass this limitation and allow global package installation using pip, the control file that enforces this mode will be removed:

sudo rm /usr/lib/python3.12/EXTERNALLY-MANAGED

This action disables the restriction and restores the previous behavior of pip.
