# OpenCL Tutorials

Hey guys, each sub-directory containing tutorials is a holistic self inclusive directory, with all the necessary source code needed to run, but not necessarily to build. These tutorials require CL2.hpp but use depreciated features from opencl version 1.2. As such setting up your own system may be a tad strange.

I have included CMake files in each directory that can be run using the build.sh file, or manually. These files are to help you with the requirements, and they are quite strict. However if you have better things to do than worry about dependencies and all their nuances, then simply  use docker instead, which will create some lightweight virtualmachines for you to work with instead automatically.

You need only 2 things, docker itself, and nvidia-container-toolkit, the latter is for GPU containers so you can use nvidia GPUs from inside any given container. For further information please see the following two sources:

https://nemesyst.readthedocs.io/en/latest/docker/ while not specifically for these tutorials it gives a good summary of how to use Dockerfiles.

https://wiki.archlinux.org/index.php/Docker the holy bible of linux, which shall endow you with super powers, including usage of docker, and installation of things like nvidia-container-toolkit.

quick-start:

# create a docker image with all our sources/ everything ready
sudo docker build -t archer/opencl-tuts .

# run our docker image with all the GPUs available
sudo docker run --gpus all -it archer/opencl-tuts bash

# OR if you dont have nvidia gpus/ you dont want to use GPUs/ don't have nvidia-container-toolkit installed
sudo docker run -it archer/opencl-tuts bash

May the force be with you.
