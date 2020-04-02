# Loop from 1-10 and print each number
# Get user input for start num and end num / must convert input to int
start_num = int(input("Start from: "))
end_num = int(input("End on: "))

# Logic
while start_num <= end_num:
    print(start_num)
    start_num += 1