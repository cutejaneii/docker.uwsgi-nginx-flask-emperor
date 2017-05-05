## docker.uwsgi-nginx-flask-emperor ##

Base on  **[tiangolo/uwsgi-nginx:python2.7](https://github.com/tiangolo/uwsgi-nginx-docker)**, we also installed following software into container for use.

- uwsgi
- nginx
- flask

### What this project do ? ###

To make multiple flask applications run at the same time, we modify nginx.conf and uwsgi config, and use emperor mode to monitor the folder (/etc/uwsgi/vassals) if any .ini files add/delete/modified.

### Usage ###

To run it if you DO NOT need to volumn folder:

> docker run -d -p 9090:80 --name nginx-uwsgi-emperor cutejaneii/uwsgi-nginx-flask-emperor

To run it if you need to volumn folder:

> docker run -d -p 9393:80 --name nginx-uwsgi-emperor -v /{host_folder}/app:/app -v /{host_folder}/vassals:/etc/uwsgi/vassals cutejaneii/uwsgi-nginx-flask-emperor
