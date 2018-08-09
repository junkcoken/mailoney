# About
これはmailoneyを改造したものです。スパマーによるメール送受信確認の対策をしています。  
本家mailoney→ https://github.com/awhitehatter/mailoney

# Installation
現在hpfeedsがないと動かないっぽいので先にそれをインストールしてください  
https://github.com/rep/hpfeeds

また、postfix等のSMTPサーバが必要なのでインストールして、メールの送信ができるようにしてください。その際、25番ポートで動かさないようにポートの設定を変更してください。
設定は人それぞれ違ってくるので割愛します。

# Running example
mailney用のユーザを作成し、ユーザとホームディレクトリを切り替え、その上で操作を行ってください。
```
$ sudo adduser --disabled-password mailoney
$ sudo su - mailoney
$ git clone https://github.com/junkcoken/mailoney.git
$ cd mailoney
$ python mailoney.py -p 2525 -s [mail host name] -t schizo_open_relay &
```

## Settings
mailoney.cfgにpostfix等のメールサーバの設定を記述します。  
```
[Real mail server]
HOST = localhost   # ホスト名・ipアドレスを記述します。多くの場合はlocalhostのままで大丈夫です。
PORT = 34280       # SMTPサーバを動かしているポート番号を記述してください。
```

## IPTables example
iptablesを以下のように設定します。
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 25 -j REDIRECT --to-ports 2525
sudo iptables -A INPUT -p tcp --dport 2525 -m conntrack --ctorigdstport 25 -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --dport 2525 -j REJECT --reject-with tcp-reset
```
2525番ポート宛ての接続を受け付けているmailoneyを、25番ポートからの接続のみで受け付けるようにします。

# Usage

```
usage: mailoney.py [-h] [-i <ip address>] [-p <port>] -s mailserver -t
                   {open_relay,postfix_credcs,schizo_open_relay}

Command line arguments

optional arguments:
  -h, --help            show this help message and exit
  -i <ip address>       The IP address to listen on
  -p <port>             The port to listen on
  -s mailserver         A Name that'll show up as the mail server name
  -t {open_relay,	Type of Honeypot 
  	postfix_creds,
  	schizo_open_relay}
```

※この改造はschizo_open_relayのみ対応しています。

# ToDo 
 - [ ] Add modules for EXIM, Microsoft, others
 - [ ] Build in Error Handling
 - [X] ~~Add a Daemon flag to background process.~~
 - [X] ~~Secure this by not requiring elevated perms, port forward from port 25.~~
 - [ ] Database logging
 - [X] ~~Possible relay for test emails.~~ ←この改造で改善されました
 - [ ] Make honeypot detection more difficult
 	(e.g. fuzz mailoney with SMTP commands, catch exceptions, patch and profit)

