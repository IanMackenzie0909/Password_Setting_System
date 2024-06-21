# 預設密碼
default_pswd = "0Aa@!23"

# 輸入密碼的次數
tries = 4

# 開始進入密碼驗證循環，直到用戶輸入正確密碼或者用完所有機會
while tries > 0:
    # 請用戶輸入密碼
    input_pswd = input("奉召前來，你是我的 Master 嗎？請下指令：")
    
    # 如果用戶輸入的密碼正確，顯示契約完成消息並跳出循環
    if input_pswd == default_pswd:
        print("吾劍將隨汝同在，汝之命運將與吾共存，於此，契約完成。")
        break
    else:
        # 如果密碼錯誤，減少一次嘗試次數
        tries -= 1
        if tries == 0:
            # 如果嘗試次數用完，顯示提示消息
            print("指令多次無效，你已經被 Saber 清除！")
        else:
            # 如果還有嘗試次數，顯示剩餘嘗試次數
            print(f"指令無效，請重下指令，還有 {tries} 次機會。")