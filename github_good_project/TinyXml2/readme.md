## 1. 新建clon的工程

## 2. cmake配置
- 在cmake中添加如下指令
```
if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else()
    message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif()
```

- conan 安装debug版本

```
conan install . -s build_type=Debug --install-folder=cmake-build-debug
```

- conan安装realse 版本

```
conan install . -s build_type=Release --install-folder=cmake-build-release
```
