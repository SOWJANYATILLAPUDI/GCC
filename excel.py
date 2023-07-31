import pandas as pd

def main():
    # Take input from the user
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    # Create a DataFrame with the input data
    data = pd.DataFrame({"Roll Number": [roll_number], "Name": [name]})

    # Save the DataFrame to an Excel file
    file_name = "student_data.xlsx"
    data.to_excel(file_name, index=False)

    print("Data stored successfully in", file_name)

if __name__ == "__main__":
    main()