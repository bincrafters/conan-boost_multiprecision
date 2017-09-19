from conans import ConanFile, tools, os

class BoostMultiprecisionConan(ConanFile):
    name = "Boost.Multiprecision"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-multiprecision"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["multiprecision"]
    requires =  "Boost.Array/1.65.1@bincrafters/stable", \
                      "Boost.Assert/1.65.1@bincrafters/stable", \
                      "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Core/1.65.1@bincrafters/stable", \
                      "Boost.Functional/1.65.1@bincrafters/stable", \
                      "Boost.Integer/1.65.1@bincrafters/stable", \
                      "Boost.Lexical_Cast/1.65.1@bincrafters/stable", \
                      "Boost.Math/1.65.1@bincrafters/stable", \
                      "Boost.Mpl/1.65.1@bincrafters/stable", \
                      "Boost.Predef/1.65.1@bincrafters/stable", \
                      "Boost.Random/1.65.1@bincrafters/stable", \
                      "Boost.Rational/1.65.1@bincrafters/stable", \
                      "Boost.Smart_Ptr/1.65.1@bincrafters/stable", \
                      "Boost.Static_Assert/1.65.1@bincrafters/stable", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/stable", \
                      "Boost.Type_Traits/1.65.1@bincrafters/stable"

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