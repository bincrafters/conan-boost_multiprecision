#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostMultiprecisionConan(base.BoostBaseConan):
    name = "boost_multiprecision"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_multiprecision"
    lib_short_names = ["multiprecision"]
    header_only_libs = ["multiprecision"]
    cycle_group = "boost_cycle_group_c"
    b2_requires = ["boost_cycle_group_c"]
