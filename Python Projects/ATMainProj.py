from ATMExcept import DepositError,WithdrawError,InsuffundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
while(True):
    menu()
    try:
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                      print("Don't Try To Deposit Alnums Strs And Sysmbols")
                except DepositError:
                      print("Don't Enter -ve And Zero As Deposit Amount")
            case 2:
                try:
                     withdraw()
                except ValueError:
                       print("Don't Try To Withdraw Alnums,Strs,And Symbols")
                except WithdrawError:
                       print("Don't Enter -ve And Zero As Withdraw Amount")
                except InsuffundError:
                       print("Your Account xxxxxxxxx123 Does Not Have Suffund")
            case 3:
                    balenq()
            case 4:
                    print("Thanks For This Application")
                    break
            case _:
                print("Your Selection Of Operation Is Wrong--------Try Again")
    except ValueError:
        print("Don't Enter Alnums,Strs And Symbols For Choice_Try Again")

