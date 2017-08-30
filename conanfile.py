from conans import ConanFile, tools, os

class BoostMultiprecisionConan(ConanFile):
    name = "Boost.Multiprecision"
    version = "1.64.0"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-multiprecision"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["multiprecision"]
    requires =  "Boost.Array/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Functional/1.64.0@bincrafters/testing", \
                      "Boost.Integer/1.64.0@bincrafters/testing", \
                      "Boost.Lexical_Cast/1.64.0@bincrafters/testing", \
                      "Boost.Math/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing", \
                      "Boost.Random/1.64.0@bincrafters/testing", \
                      "Boost.Rational/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing"

                      #array3 assert1 config0 core2 functional5 integer3 lexical_cast8 math8 mpl5 predef0 random9 rational6 smart_ptr4 static_assert1 throw_exception2 type_traits3

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()