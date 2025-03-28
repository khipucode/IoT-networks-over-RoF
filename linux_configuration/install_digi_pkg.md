# Installing digi-xbee Package with pip in an Externally Managed Environment

## Problem

When attempting to install the `digi-xbee` package using `pip`, the following error is returned:

> error: externally-managed-environment

This happens because the system is configured as an *externally managed environment* (as per [PEP 668](https://peps.python.org/pep-0668/)), preventing global package installations with `pip`.

## Solution Adopted (Not the Safest)

To bypass this restriction and allow global package installation using `pip`, the control file that enforces this mode will be removed:

```bash
sudo rm /usr/lib/python3.12/EXTERNALLY-MANAGED

## Installing the digi-xbee Package

```bash
pip install digi-xbee

