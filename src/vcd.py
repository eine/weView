#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bug in pylint leading to unfound some arguments of a function
# pylint: disable=E1120
# line too long
# pylint: disable=C0301
# too many lines in module
# pylint: disable=C0302

"""
Classes to parse VCD and eVCD files

VCD Format:
The ASCII VCD file consist of header information, variable definitions,
and value changes of variables. Header information and variable definitions
are marked by a beginning keyword and ending with an $end keyword.
The value changes are a list of values for each variable with a preceding
timestamp value. Only values that had changed need to be present in the
list of value changes for each timestamp.

"""

class VCDParser(object):
    """ VCD parser class """

    def __init__(self):
        """ Class constructor """
        pass

    def set_vcd(self, path=None):
        """ Set path to VCD file """

    def load_vcd(self):
        """ Load VCD file content """

    def get_header(self):
        """ Header getter """
        pass

    def set_header(self):
        """ Header setter """
        pass

    def get_timescale(self):
        """Timescale getter"""
        pass

    def set_timescale(self):
        """Timescale setter"""
        pass

    def get_version(self):
        """Version getter"""
        pass

    def set_version(self):
        """Version setter"""
        pass



class EVCDParser(object):
    """ eVCD parser class """

    def __init__(self):
        """ Class constructor """
        pass



