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
    while True:
        confirm_pswd = input('請再輸入剛才設定的密碼: ')
        
        if password == confirm_pswd:
            print("密碼設定完成")
            return True
        else:
            print("兩次輸入不一致，請重新設定密碼")
            return False

def main():
    password = get_valid_password()
    if password:
        confirming_password(password)

if __name__ == "__main__":
    main()