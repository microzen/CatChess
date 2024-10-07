FROM ubuntu:22.04

# Install c++ and cmake
RUN apt-get update && apt-get install -y\
    cmake\
    g++\
    build-essential

# Set working directory
WORKDIR /user/src/server

RUN mkdir cpp_py_demo

COPY CMakeLists.txt ./
COPY cpp_py_demo/server.cpp ./cpp_py_demo

RUN mkdir -p build
WORKDIR /user/src/server/build

RUN cmake ..
RUN make

EXPOSE 8080

CMD ["./demo_server"]