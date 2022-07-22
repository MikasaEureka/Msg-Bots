# Msg-Bots
Collect msg-pusher bots  
Now including:  
qmsg QMSG_TOKEN  
sever酱 SERVER_TOKEN  
pushplus PUSHPLUS_TOKEN  
企业微信 EnterpriseId(企业ID) | AppId(应用ID/AgentId) | AppSecret(应用Secret) | UserUid(推送UID)  
钉钉 DD_TOKEN(机器人token) | secret(可选：创建机器人勾选“加签”选项时使用) | atuser(被@人的用户userid。选填) | atMobiles(被@人的手机号。选填) | isAtAll(是否@所有人)  

## parts use

> for servers
> `pip install -r requirements.txt` to install 

main.py : add into any py to complete push  
MsgBots.py : Bots push code  
Configs.py : Bots config  
Log.py : System and Bots debug log  
  
> .github/workflows : folder for github actions  

bots.yml : add to other yml to complete the bots init  
  ```yaml
  schedule :
    - cron: "5 16 * * *"
  ```
  set time to run actions  
  ``` yaml
  env:
    PUSHPLUS_TOKEN: ${{ secrets.PUSHPLUS_TOKEN }}
    SERVER_TOKEN: ${{ secrets.SERVER_TOKEN }}
    QMSG_TOKEN: ${{ secrets.QMSG_TOKEN }}
    EPWECHAT_TOKEN: ${{ secrets.EPWECHAT_TOKEN }}
    DD_TOKEN: ${{ secrets.DD_TOKEN }}
  ```
  set token in secrets

## checkbox

- [ ] add github actions and secrets

reference:  
https://github.com/MikasaEureka/AutoSign-Bot-msg-Pusher  
https://github.com/MikasaEureka/tianyiyunpan  
