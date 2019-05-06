#!/bin/bash
apt-get install -y --no-install-recommends \
    make gcc libncurses5-dev g++ python unzip gcc-multilib g++-multilib
wget https://github.com/buildroot/buildroot/archive/2018.02.10.tar.gz
tar -xf 2018.02.10.tar.gz 
mkdir buildroot
cd buildroot
make O=$PWD -C ../buildroot-2018.02.10 raspberrypi3_qt5we_defconfig
