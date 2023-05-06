FROM centos:8
RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN yum -y update && yum -y install vim net-tools && yum install -y epel-release && yum -y install nginx
LABEL maintainer="Qin Ke<collinsctk@qytang.com>"

ADD static /qytdjg/static/
ADD nginx.conf /etc/nginx/nginx.conf

CMD nginx
