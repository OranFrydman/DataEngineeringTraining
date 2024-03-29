#Run postgres - create container
 docker run -t \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v C:\Users\oranf\Desktop\Oran\Projects\DataTalk-Course\data-engineering-zoomcamp\01-docker-terraform\2_docker_sql \
 -p 5432:5432 \
 postgres:13
#connect to pgcli
$ winpty pgcli -h localhost -p 5432 -u root -d ny_taxi


#Pgadmin
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4


  #Combine in network

 # docker run -t \
 # -e POSTGRES_USER="root" \
 # -e POSTGRES_PASSWORD="root" \
 # -e POSTGRES_DB="ny_taxi" \
 # -v C:/Users/oranf/Desktop/Oran/Projects/DataTalk-Course/data-engineering-zoomcamp/01-docker-terraform/2_docker_sql:/var/lib/postgresql/data \
 # -p 5432:5432 \
 # --network=pg-network\
 # --name pg-database \
 # postgres:13

#change name of container after --volumes-from XXXXX
docker run -t \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  --volumes-from unruffled_euler \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13
#build docker
docker -it build taxi_ingest:001 .