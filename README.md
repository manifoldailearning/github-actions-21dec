# github-actions-21dec
```
docker run hello-world

docker pull busybox

docker run busybox

docker run busybox echo "hello from docker busybox"

docker ps

docker ps -a

docker run -it busybox sh

exit

docker rm <container_id>


docker run -d -P --name catgif manifoldailearning/catgif
docker ps
docker port catgif
docker stop catgif

docker run -p 8888:5000 --name catgif-demo manifoldailearning/catgif
docker stop catgif-demo


docker build -t catgif-dec22 .
docker run -p 8889:5000 --name catgif-demo catgif-dec22

docker build -t yourusername/image_name .
docker push yourusername/image_name
```

