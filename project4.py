data =[]

def factorial(n):
    if n==0:
        return 1
    else:
        return*factorial(n-1)

while True:
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("Main Menu:")
    print("1. Input Data")
    print("2. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("Sort Data")
    print("6. Display Dataset Statistics")
    print("Exit Program")

    choice= input("enter your choice:")

    #option1:input data
    if choice == "1":

        data = input("Enter numbers sepereted by spaces:")
        data = data.split()
        data = [int() for x in data]
        print("Data has beeb stored successfully!")

    #option 2:show summary
    elif choice =="2":
        if len(data) ==0:
            print("No data yet! Add data first.")
        else:
            print("Data summary:")
            print("Total elements:", len(data))
            print("Minimum value:", min(data))
            print("Maximum value:", max(data))
            print("Sum of all value:", sum(data))
            print("Average value:", sum(data) / len(data))

#option3:factorial using recursion
    elif choice=="3":
        num = int(input("\nEnter a number to calculate its factorial:"))
        if num< 0:
            print("Factorial not possible for negative numbers.")
        else:
            result= factorial(num)
            print("Factorial of {num} is : [result]")

#option4 : filter data by threshold using lambda
    elif choice =="4":
        if len(data) == 0:
            print("No data available. Please input data first.")
        else:
            threshold = int(input("Enter a threshold value of filter out data above this value:"))
            filtered = list(filter (lambda x:x >= threshold, data))
            print(f"Filtered Dta (values >= {threshold}):")
            print(",".join(map(str, filtered)))

# 5. Sort Data
    elif choice == "5":
        if len(data) == 0:
            print("No data available. Please input data first.")
        else:
            print("\nChoose sorting option:")
            print("1. Ascending")
            print("2. Descending")
            sort_choice = input("Enter your choice: ")
            
            if sort_choice == "1":
                data.sort()  # ascending
                print("Sorted Data in Ascending Order:")
            else:
                data.sort(reverse=True)  # descending
                print("Sorted Data in Descending Order:")
            
            print(", ".join(map(str, data)))
    
    # 6. Display Dataset Statistics - Return Multiple Values
    elif choice == "6":
        if len(data) == 0:
            print("No data available. Please input data first.")
        else:
            count, minimum, maximum, total = get_stats(data)
            avg = total / count
            print("\nDataset Statistics:")
            print(f"- Minimum value: {minimum}")
            print(f"- Maximum value: {maximum}")
            print(f"- Sum of all values: {total}")
            print(f"- Average value: {avg:.}")
    
    # 7. Exit Program
    elif choice == "7":
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.")
