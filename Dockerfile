FROM centos:centos7
MAINTAINER Jordi Prats
ENV HOME /root

RUN yum install epel-release -y
RUN yum install git -y
RUN yum install curl -y
RUN yum install python2-pip -y
RUN yum install python-setuptools.noarch -y
RUN yum install gcc gcc-c++ make -y
RUN yum install python-devel -y

RUN pip install pandas
RUN pip install stockstats
RUN pip install python-binance
RUN pip install pandas-datareader
