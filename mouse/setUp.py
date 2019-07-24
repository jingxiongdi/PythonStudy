# coding: utf-8
from distutils.core import setup
import py2exe

options = {"py2exe": {"optimize": 2}}
setup(
      options = options,
      zipfile = None,
      console=["setUp.py"],

       )