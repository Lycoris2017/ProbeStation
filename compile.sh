#!/bin/sh

## bash command to make softlinks:
## $ mkdir ./inData/; cd inData
## $ for file in /afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/24Aug2017/Sensor*; do ln -s $file .; done

## code to compile via:
#g++ -o cviv.exe CVmeas_IVmeas.cxx -I${ROOTSYS}/include -L${ROOTSYS}/lib -std=gnu++11 $(bash root-config --cflags) $(bash root-config --libs)

g++ -o sumPlot.exe sumPlot.cxx -I${ROOTSYS}/include -L${ROOTSYS}/lib -std=gnu++11 $(bash root-config --cflags) $(bash root-config --libs)

## before you run:
## $ mkdir outData

## then you can run, for instance:
## $ ./cviv.exe 32 33 55 59
## $ ./cviv.exe v2 33 42
#./cviv.exe 31 32 33 34 35 36 37 38 39
#./cviv.exe 40 41 42 43 44 45 46 47 48 49
#./cviv.exe 50 51 52 53 54 55 56 57 58 59
#./cviv.exe v2 31 32 33 42 43 58
#./cviv.exe v3 58
