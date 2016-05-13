```
docker run -d --name redis growdane/redis
```

```
docker run -p 4567 --name webapp --link redis:db -t -i -v $PWD/webapp:/opt/webapp growdane/sinatra /bin/bash
```

