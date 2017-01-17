# --*-- coding:UTF-8 --*--
import telnetlib
import time

user_ip = raw_input("请输入用户IP地址：")
floor = raw_input("请输入楼层[F1|F2|F3|F4|F5]:")
if floor == 'F5':
    s3_ip = '192.168.13.225'
elif floor == 'F4':
    s3_ip = '192.168.13.193'
elif floor == 'F3':
    s3_ip = '192.168.13.161'
elif floor == 'F2':
    s3_ip = '192.168.13.129'
elif floor == 'F1':
    s3_ip = '192.168.13.97'
else:
    print("输入的楼层错误！")
    exit()
enter_key = '\r\n'
s3_username = '20017'
s3_password = 'xxjsb@ks.net'
s2_username = 'sunzhaozeng'
s2_password = 'szlch@781213'
delay_sec = 5
s2_ip = ''
port = '23'
command_arp = 'dis arp | in ' + user_ip

tn = telnetlib.Telnet()
tn.set_debuglevel(0)
try:
    tn.open(s3_ip, port)
except Exception as e:
    print(e)

tn.read_until('Username', 5)
tn.write(s3_username + enter_key)
tn.read_until('Password', 5)
tn.write(s3_password + enter_key)
time.sleep(delay_sec)
res = tn.read_very_eager()

if res.find('failed') != -1:
    print("Login " + s3_ip + " failed!")
    exit()
else:
    print("Login " + s3_ip + " access!")

tn.write(command_arp + enter_key)
time.sleep(delay_sec)
res = tn.read_very_eager()

line = res.split()[17:]
for i in range(len(line)):
    if line[i] == user_ip:
        user_mac = line[i+1]
        interface = 'g1/0/' + line[i+3].split('/')[2]

command_lldp = 'dis lldp neigh int ' + interface

tn.write(command_lldp + enter_key)
time.sleep(delay_sec)
res = tn.read_very_eager()

line = res.split()
for l in line:
    if l.__contains__('192.168.13'):
        # print l
        s2_ip = l
tn.close()

if s2_ip:
    command_mac = 'dis mac-add ' + user_mac
    tn = telnetlib.Telnet()
    tn.set_debuglevel(0)
    try:
        tn.open(s2_ip, port)
    except Exception as e:
        print(e)

    tn.read_until('Username', 5)
    tn.write(s2_username + enter_key)
    tn.read_until('Password', 5)
    tn.write(s2_password + enter_key)
    time.sleep(delay_sec)
    res = tn.read_very_eager()

    if res.find('failed') != -1:
        print("Login " + s2_ip + "failed!")
        exit()
    else:
        print("Login " + s2_ip + " access!")
    if floor == 'F5':
        tn.write('super' + enter_key)
        tn.read_until("Password", 5)
        tn.write('ks@2016' + enter_key)
    tn.read_until(">", 5)

    tn.write(command_mac + enter_key)
    time.sleep(delay_sec)
    res = tn.read_very_eager()
    line = res.split()
    sw_name = ''
    sw_port = ''
    for l in line:
        if l.__contains__(floor):
            sw_name = l
        if l.__contains__('GigabitEthernet'):
            sw_port = l

    print "用户接入交换机信息：【名称: " + sw_name + " IP地址：" + s2_ip + " 端口:" + sw_port + "】"

    tn.close()
else:
    print("User ip is wrong!")
