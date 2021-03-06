import sys

def from_one_to_1_left_31(sequence_file_name, sum_file_name):
    sequence_file = open(sequence_file_name, 'w')  

    sum = 0
    for i in range(1 << 31):
        num = 1 << i
        print(num)
        sequence_file.write(str(num) + '\n')
        sum += num

    sequence_file.close() 

    sum_file = open(sum_file_name, 'w')
    sum_file.write("sum:\n" + str(sum) + "\n")
    sum_file.close()

def main():
    if len(sys.argv) != 3:
        print("usage: \n$ python sequence_file.txt sum_file.txt")
        sys.exit(1)

    from_one_to_1_left_31(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

