#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from conans import ConanFile, CMake, tools


class Ooh323cConan(ConanFile):
    name = "ooh323c"
    version = "da48d3f"
    description = "ooh323c"
    url = "http://github.com/theirix/conan-ooh323c"
    homepage = "https://github.com/theirix/ooh323c"
    license = "Custom"
    exports = ["LICENSE.md"]
    exports_sources = ['CMakeLists.txt']
    generators = 'cmake'
    source_subfolder = "source_subfolder"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"

    def source(self):
        self.run("git clone https://github.com/theirix/ooh323c %s" % self.source_subfolder)
        with tools.chdir(self.source_subfolder):
            self.run("git checkout %s" % self.version)

        os.rename(os.path.join(self.source_subfolder, "CMakeLists.txt"),
                  os.path.join(self.source_subfolder, "CMakeListsOriginal.txt"))
        shutil.copy("CMakeLists.txt",
                    os.path.join(self.source_subfolder, "CMakeLists.txt"))

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder)
        cmake.build()

    def package(self):
        self.copy("COPYING", dst="licenses", src=self.source_subfolder)

        self.copy("*.h", dst="include", src=os.path.join(self.source_subfolder, "src"), keep_path=False)

        if self.options.shared:
            if self.settings.os == "Macos":
                self.copy(pattern="*.dylib", dst="lib", keep_path=False)
            else:
                self.copy(pattern="*.so*", dst="lib", keep_path=False)
        else:
            self.copy(pattern="*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
