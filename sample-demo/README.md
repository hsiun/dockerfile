### build docker image ###
```
docker build -t growdane/ngin .
```

### run a docker contain ###
```
docker run -d -p 80 --name website -v $PWD/website:/var/www/html/website growdane/nginx nginx
```
