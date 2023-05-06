FROM centos:8
RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN yum -y update && yum -y install gcc python3-devel && yum -y install python3 && yum -y install net-tools && yum -y install dos2unix
LABEL maintainer="Qin Ke<collinsctk@qytang.com>"

ADD djg_dir /djg

COPY requirement.txt .
RUN pip3 install -i https://pypi.douban.com/simple/ -r requirement.txt

ENV RUN_PORT=8001

EXPOSE $RUN_PORT

WORKDIR /djg/qyt_djg/
COPY init-db.sh .
#CMD uwsgi --ini /djg/qyt_djg/uwsgi.ini
CMD dos2unix init-db.sh && chmod +x init-db.sh && ./init-db.sh