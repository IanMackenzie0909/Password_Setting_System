import re

def get_valid_password():
    while True:
        pswd = input('請設定密碼 (密碼必須是 7 到 12 個字元，必須包含大寫英文字母、小寫英文字母、數字、特殊符號)，或者直接按下 Enter 跳出:')
        
        if not pswd:
            print("跳出密碼設定")
            return None
        
        if validate_password(pswd):
            return pswd

def validate_password(pswd):
    if not (7 <= len(pswd) <= 12):
        print("密碼長度必須是 7 到 12 個字元")
        return False
    elif not re.search("[a-z]", pswd):
        print("密碼必須包含小寫英文字母")
        return False
    elif not re.search("[A-Z]", pswd):
        print("密碼必須包含大寫英文字母")
        return False
    elif not re.search("[0-9]", pswd):
        print("密碼必須包含數字")
        return False
    elif not re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", pswd):
        print("密碼必須包含特殊符號")
        return False
    else:
        return True

def confirming_password(password):
    tries = 4
    while tries > 0:
        confirm_pswd = input('請再輸入剛才設定的密碼: ')
        
        if password == confirm_pswd:
            print("密碼設定完成")
            return True
        else:
            tries -= 1
            if tries == 0:
                print("兩次輸入不一致，你已經被魔法師清除！")
                # 如果使用者被清除了，重新設定密碼
                return False
            else:
                print(f"兩次輸入不一致，請重新輸入，你還有 {tries} 次機會。")
    return False

def main():
    password = get_valid_password()
    if password:
        while not confirming_password(password):
            # 重新設定密碼
            print("重新設定密碼")
            password = get_valid_password()
            if not password:
                break
        else:
            # Here you can add any additional logic after successful password setup
            print("密碼已驗證")

if __name__ == "__main__":
    main()