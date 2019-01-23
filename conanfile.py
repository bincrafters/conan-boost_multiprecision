#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostMultiprecisionConan(base.BoostBaseConan):
    name = "boost_multiprecision"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_multiprecision"
    lib_short_names = ["multiprecision"]
    header_only_libs = ["multiprecision"]
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_integer",
        "boost_lexical_cast",
        "boost_math",
        "boost_mpl",
        "boost_predef",
        "boost_random",
        "boost_rational",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits"
    ]


