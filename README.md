### 说明 ###
这里的是一个我所有Dockerfile的集合，包括自己写的和书上学习来的，放在一个项目中便于管理和使用，使用-demo结尾的是书上的例子，没有的则是自己根据需要写的。

### Jekyll-demo ###
通过下面命令运行容器，并且把宿主机上的james_blog这个文件挂载到容器的/data目录下
```
docker run -v /root/dockerfile/jekyll-demo/james_blog:/data/ --name growdane_blog growdane/jekyll
```

把growdane/apache里的所有卷（两个）都加到apache这个容器中，以实现容器间的文件共享
```
docker run -d -P --volumes-from growdane_blog growdane/apache
```

### Sample-demo ###
创建镜像
```
docker build -t growdane/nginx .
```

运行容器
```
docker run -d -p 80 --name website -v $PWD/website:/var/www/html/website growdane/nginx nginx
```

### Sintra-demo ###
创建一个redis容器
```
docker run -d --name redis growdane/redis
```
创建一个sinatra容器，并且将他通过link连接到redis，这个命令执行后会进入容器
```
docker run -p 4567 --name webapp --link redis:db -t -i -v $PWD/webapp:/opt/webapp growdane/sinatra /bin/bash
```


### Tomcat-demo ###

运行fetcher容器下载示例war文件
```
docker run -t -i --name sample growdane/fetcher https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/sample.war
```

查看卷在宿主机上的目录
```
docker inspect -f "{{ .Volumes }}" sample #试验的时候好像获取不到。。
```

运行tomcat容器
```
docker run --name sample_app --volumes-from sample -d -P growdane/tomcat7
```

访问sample项目
```
curl 0.0.0.0::32792/sample/
```
