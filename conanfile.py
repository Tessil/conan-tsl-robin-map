from conans import ConanFile, CMake, tools
import os

class TslRobinMapConan(ConanFile):
    name = "tsl-robin-map"
    version = "0.6.1"
    license = "MIT"
    description = "C++ implementation of a fast hash map and hash set using robin hood hashing."
    homepage = "https://github.com/Tessil/robin-map"
    url = "https://github.com/Tessil/conan-tsl-robin-map"
    exports = "LICENSE"

    def source(self):
        tools.get("%s/archive/v%s.tar.gz" % (self.homepage, self.version))

    def package(self):
        self.copy("LICENSE", dst="licenses", keep_path=False, ignore_case=True)
        
        cmake = CMake(self)
        cmake.configure(source_folder="robin-map-%s" % (self.version))
        cmake.install()

    def package_id(self):
        self.info.header_only()
