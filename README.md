[ ![Download](https://api.bintray.com/packages/theirix/conan-repo/ooh323c%3Atheirix/images/download.svg) ](https://bintray.com/theirix/conan-repo/ooh323c%3Atheirix/_latestVersion)
[![Build Status](https://travis-ci.org/theirix/conan-ooh323c.svg)](https://travis-ci.org/theirix/conan-ooh323c)

# conan-ooh323c

[Conan.io](https://conan.io) package for [ooh323c](https://github.com/traviscross/ooh323c) library

The packages generated with this **conanfile** can be found in conan.io.

## Build packages

    $ pip install conan_package_tools
    $ python build.py
    
## Upload packages to server

    $ conan upload ooh323c/<version>@theirix/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install ooh323c/<version>@theirix/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    ooh323c/<version>@theirix/stable

    [options]
    ooh323c:shared=true # false
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
