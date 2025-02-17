from ATMExcept import DepositError,WithdrawError,InsuffundError
bal = 50000-0
def deposit():
    damt=float(input("Enter Your Deposit Amount:"))
    if (damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Your Account xxxx123 Balance INR:{}".format(bal))
        print("Now Your Accoount xxxx123 Balance INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter Your Withdraw Amount:"))
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InsuffundError
    else:
        bal=bal-wamt
        print("Your Account xxxxxx123 Debited With INR:{}".format(wamt))
        print("Now Your Account xxxxx123 Balance INR:{}".format(bal))
def balenq():
        print("Your Account xxxxx123 Balance INR:{}".format(bal))