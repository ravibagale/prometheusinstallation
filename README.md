# prometheusinstallation

- copy these all lines and execute as one command
- ------------------------------------------------------

sudo tee /etc/yum.repos.d/prometheus.repo <<EOF
[prometheus]
name=Prometheus
baseurl=https://packagecloud.io/prometheus-rpm/release/el/7/x86_64
repo_gpgcheck=1
enabled=1
gpgkey=https://packagecloud.io/prometheus-rpm/release/gpgkey https://raw.githubusercontent.com/lest/prometheus-rpm/master/RPM-GPG-KEY-prometheus-rpm
gpgcheck=1
metadata_expire=300
EOF
-----------------------------------------------------------------

- sudo yum update -y
- sudo yum -y install prometheus2 node_exporter
- rpm -qi prometheus2
- sudo systemctl start prometheus node_exporter
- systemctl status prometheus.service node_exporter.service
- add port 9090 in security group
- copy ec2 public IP and paste in browser with port no 9090
- now you should see prometheus dashboard

#sudo nano  /etc/prometheus/prometheus.yml



