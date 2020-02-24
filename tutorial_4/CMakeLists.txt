# MIT License
# ===========
#
# Copyright (c) 2019 George Onoufriou (GeorgeRaven, archer, DreamingRaven)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# sets versions and names of project
cmake_minimum_required(VERSION 3.7)
project(opencl_tutorial_1)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
# specify our compiled binaries name
set(BINARY_NAME tut4)
# specify all our cpp files names
set(CPP_FILES tut4.cpp utils.h CImg.h)

# build our project executable, and link opencl lib
find_package(OpenCL 2 REQUIRED)
# find x11 for linux desktop
find_package(X11)
# get thread library used in the tutorials
find_package(Threads REQUIRED)
# find boost for tut4 and up
find_package(Boost REQUIRED)

add_executable(${BINARY_NAME} ${CPP_FILES})
target_link_libraries(tut4 OpenCL::OpenCL ${X11_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT} ${Boost_LIBRARIES})

# copy kernel files over to binary directory so it can access them
# configure_file( ${CMAKE_CURRENT_SOURCE_DIR}/kernels/my_kernels.cl ${CMAKE_CURRENT_BINARY_DIR}/kernels/my_kernels.cl COPYONLY)
# copy our images where they should be relative to the compiled binary from above
# configure_file( ${CMAKE_CURRENT_SOURCE_DIR}/test.ppm ${CMAKE_CURRENT_BINARY_DIR}/test.ppm COPYONLY)
