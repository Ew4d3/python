def main():
    var1=int(input("Enter a number: "))
    var2=int(input("Enter another number: "))

    if var1+var2<=1000:
        print("product is", var1*var2)
    else:
        print("sum is", var1+var2)


main()