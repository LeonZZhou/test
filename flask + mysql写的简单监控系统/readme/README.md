flask + mysql写的简单监控系统 - 为程序员服务.html(http://ju.outofmemory.cn/entry/126800)

python2.7+flask+mysql

flask.py
    line 8:xxx->your mysql root passwd.
moniItems.py
    line 85:xxxip->server ip address.

CentOS7
    firewall-cmd --permanent --add-port=8888/tcp
    firewall-cmd --permanent --add-port=8888/udp
    firewall-cmd --reload