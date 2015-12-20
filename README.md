Dockerised Super Simple Web Server
==================================

This Docker container will spawn a Python BaseHTTPServer instance that reports
some information on the incoming HTTP connection. It's designed for testing
load balancer configurations and the like. It's not expected this will do
anything useful for anyone.

Usage
-----
Build the Docker image as follows:

    $ cd docker-ssws
    $ docker build -t ssws .

or, pull from the Docker registry:

    $ docker pull jfautley/ssws

Run the container as follows:

    $ docker run --rm -d -P ssws

The container will expose port 80 for incoming connections.
