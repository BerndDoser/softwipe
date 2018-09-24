"""
This module contains all information concerning the tools that are used by softwipe.
"""

import collections
import enum


Tool = collections.namedtuple('Tool', ['exe_name', 'install_name', 'install_via'])
Via = enum.Enum('Via', 'PACKAGE_MANAGER PIP')


# The exe_names may be modified to contain a full path
class TOOLS:
    CLANG = Tool('clang', 'clang', Via.PACKAGE_MANAGER)
    CLANGPP = Tool('clang++', 'clang', Via.PACKAGE_MANAGER)
    CMAKE = Tool('cmake', 'cmake', Via.PACKAGE_MANAGER)
    MAKE = Tool('make', 'make', Via.PACKAGE_MANAGER)
    COMPILEDB = Tool('compiledb', 'compiledb', Via.PIP)
    CPPCHECK = Tool('cppcheck', 'cppcheck', Via.PACKAGE_MANAGER)
    SPLINT = Tool('splint', 'splint', Via.PACKAGE_MANAGER)
    FLAWFINDER = Tool('flawfinder', 'flawfinder', Via.PIP)
    CLANG_TIDY = Tool('clang-tidy', 'llvm', Via.PACKAGE_MANAGER)
    LIZARD = Tool('lizard', 'lizard', Via.PIP)