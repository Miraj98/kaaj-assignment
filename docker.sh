aws ecr get-login-password --region ap-south-1 --profile hallparty-ecr | docker login --username AWS --password-stdin 254355196439.dkr.ecr.ap-south-1.amazonaws.com
docker build -t kaaj-fastapi . --platform linux/amd64
docker tag kaaj-fastapi:latest 254355196439.dkr.ecr.ap-south-1.amazonaws.com/kaaj-fastapi:latest
docker push 254355196439.dkr.ecr.ap-south-1.amazonaws.com/kaaj-fastapi:latest
