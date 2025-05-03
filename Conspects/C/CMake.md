# CMake

```
cmake_minimum_required(VERSION 3.10)
project(project_name)

set(CMAKE_C_STANDARD 17 REQUIRED True)
add_definitions(-DOPENCV)
include_directories("path/to/includes/of/library")
link_directories("path/to/static/libs")
add_executable(project_name
     main.c
      ...
)
```
После созданияCMake файла запускать программу через `cmake -S . -B build2`, затем `cmake --build .\build2\ --config Release`
