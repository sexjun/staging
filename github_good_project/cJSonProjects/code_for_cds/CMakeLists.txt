cmake_minimum_required(VERSION 3.17)
project(code_for_cds C)

# 1. 新增头文件
#include_directories(../cJSON)

set(CMAKE_C_STANDARD 99)

# 2. 将所有代码路径存到变量:SOURCES
set(SOURCES
        main.c
        ../cJSON/cJSON.c
        )

# 3. 设置 cjson的路径
set (CJSON_PATH
        ../cJSON)

# 最后一步:编译
add_executable(code_for_cds ${SOURCES})

# 头文件
message("包含头文件: cjson 路径为: ${CJSON_PATH}")
target_include_directories(code_for_cds
        PRIVATE
            ${CJSON_PATH}/
        )