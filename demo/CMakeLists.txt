# CMake version
cmake_minimum_required(VERSION 3.0)

project(CatChess_DEMO VERSION 1.0)

# Cpp standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(demo_server cpp_py_demo/server.cpp)