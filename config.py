# TG机器人的令牌，tg找@BotFather创建机器人即可获取
TOKEN = 'token'
# pikpak账号，可以为手机号、邮箱，支持任意多账号
USER = ["example_user1", "example_user2"]
# 账号对应的密码，注意与账号顺序对应！！！
PASSWORD = ["example_password1", "example_password2"]
# 以下分别为aria2 RPC的协议（http/https）、host、端口、密钥
ARIA2_HTTPS = False
ARIA2_HOST = "example.aria2.host"
ARIA2_PORT = "port"
ARIA2_SECRET = "secret"
# aria2下载根目录
ARIA2_DOWNLOAD_PATH = "/mnt/sda1/aria2/pikpak"
# 可以自定义TG API，也可以保持默认
TG_API_URL = 'https://api.telegram.org'

#you-get下载目录
YOUGET_DOWNLOAD_PATH = "/root/download"

#rclone默认需要备份上传的目录
RCLONE_LOCAL_PATH = "/root/download"
#rclone默认远程存储路径
RCLONE_REMOTE_PATH = "alist:/teambition"