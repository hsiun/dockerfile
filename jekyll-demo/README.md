```
docker run -v /root/dockerfile/jekyll-demo/james_blog:/data/ --name growdane_blog growdane/jekyll

```

```
docker run -d -P --volumes-from growdane_blog growdane/apache
```
