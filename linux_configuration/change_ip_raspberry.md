Solução: Redefinir IP estático via systemd-networkd (alternativa ao dhcpcd)
Se dhcpcd está travando, podemos parar de usá-lo e configurar o IP estático com systemd-networkd, que é nativo no Linux moderno.

1. Desabilitar o dhcpcd
$ sudo systemctl stop dhcpcd
$ sudo systemctl disable dhcpcd

2. Criar configuração de rede para IP estático
Crie um arquivo:
sudo nano /etc/systemd/network/eth0.network

E coloque:

[Match]
Name=eth0

[Network]
Address=192.168.1.100/24
Gateway=192.168.1.1
DNS=8.8.8.8

Substitua eth0 pelo nome correto da sua interface (confirme com ip link).

3. Ativar systemd-networkd
sudo systemctl enable systemd-networkd
sudo systemctl start systemd-networkd

4. Reiniciar e verificar
sudo reboot
   
