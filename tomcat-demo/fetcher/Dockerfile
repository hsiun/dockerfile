FROM ubuntu:14.04
MAINTAINER Gao Xiong <growdane@gmail.com>
ENV REFRESHED_AT 2016-5-14

RUN apt-get -yqq update
RUN apt-get -yqq install wget

VOLUME [ "/var/lib/tomcat7/webapps/" ]
WORKDIR /var/lib/tomcat7/webapps/

# 用于下载，可以在docker创建的时候添加下载链接作为参数
ENTRYPOINT [ "wget" ]
CMD [ "-?" ]


