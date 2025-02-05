FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 pip vim neovim git curl wget unzip build-essential libpng-dev libjpeg-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libgeos-dev libbz2-dev

WORKDIR /home/user

RUN pip install numpy scipy matplotlib pandas scikit-learn scikit-image opencv-python opencv-python-headless --break-system-packages

CMD ["nvim", "--daemon"]
