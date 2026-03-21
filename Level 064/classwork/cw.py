# 1)შექმენით ფუნქცია და დაარქვი სახელი say_my_name()

# შენმა ფუნქციამ უნდა დაპრინტოს შემდეგი ტექსტი --> "my name is ..."   <---შეიყვან შენ სახელს

# შემდეგ შენი დავალებაა რომ გამოიძახო ფუნქცია რომ ნახო შენი ფუნქციის შედეგი,

# გამოიძახე ფუნქცია რამდენჯერმე რომ ნახო შენი ფუნქციის შედეგი რამდენჯერმე




# def say_my_name():
#     print("my name is anano")
# say_my_name()
# say_my_name()
# say_my_name()
# say_my_name()


# 2)შექმენი ფუნქცია სახელად check_even()

# ფუნქციის შიგნით შექმენი ცვლადი სადაც შიინახავ რაიმე რიცხვს

# შემდეგ შეამოწმე-->

# თუ ცვლადში შენახული რიცხვი არის ლუწი --- ფუნქციამ დააბრუნოს ==> "this number is even"

# სხვა შემთხვევაში --- ფუნქციამდ ააბრუნოს ==> "this number is odd"


# def check_even():
#     number = 7  

#     if number % 2 == 0:
#         return "this number is even"
#     else:
#         return "this number is odd"
# result = check_even()
# print(result)


name=input("enter your name:")
while True:
    if name != "anano":
        print("try again")
        name=input("enter your name:")
    else:
        print("nice")
        break
    
    