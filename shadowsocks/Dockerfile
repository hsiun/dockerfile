# Version: 0.0.1

# Pull base image
FROM centos:6

MAINTAINER Gao Xiong "growdane@gmail.com"

# Install openssl-devel
RUN yum -y install openssl-devel

# Install make and another devople tools
RUN yum -y install gcc gcc-c++ automake autoconf libtool make

# Install git 
RUN yum -y install git

# Pull shadowsocks and install
RUN cd /root && git clone https://github.com/madeye/shadowsocks-libev.git
RUN cd /root/shadowsocks-libev && ./configure && make && make install

# Expose ports
EXPOSE 8388

# Define default command
ENTRYPOINT cd /root/shadowsocks-libev && ss-server -p 8388 -k fuckgfw10086
