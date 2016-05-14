通过下面命令运行容器，并且把宿主机上的james_blog这个文件挂载到容器的/data目录下
```
docker run -v /root/dockerfile/jekyll-demo/james_blog:/data/ --name growdane_blog growdane/jekyll
```

把growdane/apache里的所有卷（两个）都加到apache这个容器中，以实现容器间的文件共享
```
docker run -d -P --volumes-from growdane_blog growdane/apache
```
