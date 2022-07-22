# 推送配置
config = {
    # 推送方式
    # 支持qmsg酱 server酱 企业微信推送 钉钉机器人推送
    # qmsg,server,epwc,dingtalk
    # 为空或False则不进行推送
    "PushMode":"dingtalk",
    # 推送配置
    "PushKey":{
        # qmsg酱配置
        "Qmsg":"",
        # Server酱配置
        "Server":"",
        # 企业微信推送配置
        # 获取配置可以看 Server酱 的企业微信配置 https://sct.ftqq.com/forward
        "Epwc":{
            # 企业ID
            "EnterpriseId":"",
            # 应用ID/AgentId
            "AppId":"",
            # 应用Secret
            "AppSecret":"",
            # 推送UID
            "UserUid":""
        },
         # 钉钉机器人token获取 https://open.dingtalk.com/document/robots/custom-robot-access
         # 复制access_token=后面的token
        "Dingtalk":{
            # 机器人token
            "token":"",
            # 可选：创建机器人勾选“加签”选项时使用
            "secret":"",
            # 被@人的用户userid。选填
            "atuser":"",
            # 被@人的手机号。选填
            "atMobiles":"",
            # 是否@所有人。
            "isAtAll":False
        }
    }
}
