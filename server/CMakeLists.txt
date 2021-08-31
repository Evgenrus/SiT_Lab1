cmake_minimum_required(VERSION 3.20)
project(Lab1 C)

set(CMAKE_C_STANDARD 99)
link_libraries(ws2_32 wsock32)

add_executable(Lab1 server.c)
