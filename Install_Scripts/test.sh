# /bin/bash
docker run -w / -it ubuntu sh -uec '
  apt-get update -y
  apt-get install -y wget tar vim less
  wget https://github.com/sayanarijit/xplr/releases/latest/download/xplr-linux.tar.gz
  tar -xzvf xplr-linux.tar.gz
  ./xplr
'

