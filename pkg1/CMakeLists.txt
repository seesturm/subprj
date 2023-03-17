cmake_minimum_required(VERSION 3.15)
project(pkg1 CXX)




add_library(pkg1 src/pkg1.cpp)
target_include_directories(pkg1 PUBLIC include)



set_target_properties(pkg1 PROPERTIES PUBLIC_HEADER "include/pkg1.h")
install(TARGETS pkg1)
