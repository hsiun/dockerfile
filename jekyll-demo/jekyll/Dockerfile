# Version 0.0.1
FROM ubuntu:14.04
MAINTAINER Gao Xiong <growdane@gmail.com>

ENV REFRESHED_AT 2016-5-14

RUN apt-get -yqq update
RUN apt-get -yqq install ruby ruby-dev make nodejs
# RUN gem install --no-rdoc --no-ri jekyll
# The default command apparently tries to install Jekyll 3, which was released on October 27th 2015. The 2.5 version still works with Ruby 1.9.3, and its quite allright for me, probably for you too.
RUN gem install --no-rdoc --no-ri jekyll -v 2.5
# data是工作目录,存放网站的源码，/var/www/html是网站内容存放的目录
VOLUME /data
VOLUME /var/www/html
WORKDIR /data

# 每次重新启动镜像都会运行这个命令，相当于就是更新了网站
ENTRYPOINT ["jekyll", "build", "--destination=/var/www/html"]

