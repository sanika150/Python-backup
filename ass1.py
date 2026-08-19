import threading

def Prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_thread(No):
    prime=[n for n in No if Prime(n)]
    print("Prime numbers: ",prime)

def non_prime_thread(No):
    non_prime=[n for n in No if not Prime(n)]
    print("Non-Prime numbers: ",non_prime)

   


def main():
    size = 0
    Value =0

    print("Enter the number of elements:")
    size = int(input())

    Data = list() #create list

    print("Enter the elements :")
    for i in range(size):
        Value = int(input())
        Data.append(Value)
    
    t1 = threading.Thread(target=prime_thread,args=(Value,))
    t2 = threading.Thread(target=non_prime_thread,args=(Value,))
    
    t1.start()
    t2.start()
    

    t1.join()
    t2.join()
   

 

if __name__ == "__main__":
    main()