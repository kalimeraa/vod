NETWORK_NAME=vod_network
if [ -z $(docker network ls --filter name=^${NETWORK_NAME}$ --format="{{ .Name }}") ] ; then 
     echo 'creating docker vod_network'
     docker network create ${NETWORK_NAME} ; 
     
fi

echo 'Running docker-compose up command... on genre-service'
cd genre-service/ && docker-compose up -d --build
echo 'Running docker-compose up command... on content-service'
cd ../content-service/ && docker-compose up -d --build