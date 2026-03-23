# Solução: Redefinir IP estático via systemd-networkd (alternativa ao dhcpcd)

Se o **dhcpcd** está travando, podemos parar de usá-lo e configurar o IP estático com **systemd-networkd**, que é nativo no Linux moderno.

---

## 1️⃣ Desabilitar o dhcpcd

```bash
sudo systemctl stop dhcpcd
sudo systemctl disable dhcpcd
```

---

## 2️⃣ Criar configuração de rede para IP estático

Crie o arquivo:

```bash
sudo nano /etc/systemd/network/eth0.network
```

E adicione:

```ini
[Match]
Name=eth0

[Network]
Address=192.168.1.100/24
Gateway=192.168.1.1
DNS=8.8.8.8
```

> ⚠️ Substitua **eth0** pelo nome correto da sua interface
> (confirme com o comando `ip link`).

---

## 3️⃣ Ativar o systemd-networkd

```bash
sudo systemctl enable systemd-networkd
sudo systemctl start systemd-networkd
```

---

## 4️⃣ Reiniciar e verificar

```bash
sudo reboot
```

Após reiniciar, verifique o IP configurado com:

```bash
ip a
```

