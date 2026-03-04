time=18
x='gudevg' if time>18 else'gudafn'
print(x)
is_data_cleaned=True
type1="list"if not is_data_cleaned else "tuple"
print(type1)
type2="list"if is_data_cleaned else "tuple"
print(type2)
stored_usernmae='Indian'
stored_password='Indian@123'
input_username=input('enter usernmae:')
input_password=input('enter password:')
login_status='sucessfully logedin'if(input_username==stored_usernmae and input_password==stored_password) else 'invalid credentials'
print(login_status)
num=int(input("enter the number:"))
op='positive'if num>0 else 'negative'
print(op)
num=int(input("enter the number:"))
op='even'if num%2==0 else 'odd'
print(op)
op='even'if num&1==0 else 'odd'
print(op)