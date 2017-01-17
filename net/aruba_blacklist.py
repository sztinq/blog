# --*-- coding:UTF-8 --*--
import telnetlib
import time

user_mac = raw_input("请输入MAC地址：")
enter_key = '\r\n'
username = 'admin'
password = 'xxjsb@ARUBA2016'
enable_pwd = 'ksaruba2015'
delay_sec = 5
aruba_ip = '192.168.95.100'
port = '23'
add_mac = 'stm add-blacklist-client ' + user_mac

tn = telnetlib.Telnet()
tn.set_debuglevel(1)
try:
    tn.open(aruba_ip, port)
except Exception as e:
    print(e)
tn.read_until('User:', 5)

tn.write(username + enter_key)
tn.read_until('Password:', 5)
tn.write(password + enter_key)
res = tn.read_very_eager()

if res.find('WARNING') != -1:
    print("Login " + aruba_ip + " failed!")
    exit()
else:
    print("Login " + aruba_ip + " access!")
tn.read_until('>', 5)
tn.write('en'+ enter_key)
tn.read_until('Password:', 5)
tn.write(enable_pwd + enter_key)
time.sleep(delay_sec)
tn.write('configure t' + enter_key)
time.sleep(delay_sec)
tn.read_until('config', 5)
tn.write(add_mac+ enter_key)
time.sleep(1)
tn.write('exit' + enter_key)
time.sleep(1)
tn.write('write memory' + enter_key)
time.sleep(1)
tn.write('exit' + enter_key)
tn.close()
