# flask + mysql写的简单监控系统

---

flask + mysql写的简单监控系统 - 为程序员服务.html(http://ju.outofmemory.cn/entry/126800)  

python2.7+flask+mysql  

运行前环境：  
flask.py  
&emsp;line 8:xxx->your mysql root passwd.  

moniItems.py  
&emsp;line 85:xxxip->server ip address.  

CentOS7  
&emsp;firewall-cmd --permanent --add-port=8888/tcp  
&emsp;firewall-cmd --permanent --add-port=8888/udp  
&emsp;firewall-cmd --reload  
