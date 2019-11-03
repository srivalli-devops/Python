import mysql.connector
class Transaction:
    con=''
    def do():
        try:
            Transaction.con = mysql.connector.connect(user='root',password='root',host='localhost',database='student')
            print("Connected to database")

            Transaction.con.autocommit = False
            print("auto commit to false..")
            
            cur = Transaction.con.cursor()

            accno = int(input("Enter accno : "))
            
            cur.execute("select balance from account where accno="+str(accno))
            row = cur.fetchone()
            balance = row[0]
            print("Balance is : ", balance)

            amount = int(input("Enter amt to transfer :"))

            dest_acc = int(input("Enter accno to transfer : "))
            if amount<=balance:
                balance = balance-amount
                cur.execute("update account set balance="+str(balance)+" where accno="+str(dest_acc))
                Transaction.con.commit()
            else:
                print("Low balance in account to transfer")
            
        except Exception as e:
            print("Exception : ",e)
            Transaction.con.rollback()

        finally :
            if Transaction.con != '':
                Transaction.con.close()
                print("Database released...")
            else:
                print("No connection to database")
                
class Banking:
    def main():
        Transaction.do()
        return
    
if __name__ == "__main__":
    Banking.main()
