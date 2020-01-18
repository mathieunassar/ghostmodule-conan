cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)
set(CMAKE_CXX_FLAGS "-std=c++14")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(connection_extension_daemon connection_extension_daemon.cpp)
message(${CONAN_LIB_DIRS})
target_link_libraries(connection_extension_daemon ${CONAN_LIBS})
