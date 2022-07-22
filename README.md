# XYZCarPlates4


## BaiDu离线库使用教程
* 将LinuxSDK拷贝到设备上
* 然后进入SDK文件夹下，sh run.sh 获取device_id
* 登陆Baidu智能云控制台，找到sdk离线激活，将device_id拷贝到激活处
* 激活成功，下载license文件，拷贝到XYZCarPlates4/_RESOURCE/LICENSE下
* 将license.key里的序列号复制粘贴到XYZCarPlates4/PlatesHunter.py里

## 第一次启动程序需要编译
* cd XYZCarPlates4/BaiduAPI
* mkdir build
* cd build
* cmake ..
* make
* 然后进入lib下
* sh install.sh  有可能需要sudo


## 树莓派摄像头启用
* sudo nano /boot/config.txt
* 找到hdmi_force_hotplug=1 取消注释
* camera_auto_detect=1 改成=0