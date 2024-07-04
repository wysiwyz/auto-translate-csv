import csv
import random
from faker import Faker
from faker.providers import company

def generate_test_csv(filename: str, num_rows: int = 60):
    """
    生成 .csv 檔測試用資料, 其中欄位 code_msg 跟 description 為可讀的英文句子

    :param filename: 要生成的 csv 檔案名稱
    :param num_rows: 要生成幾行假資料 (預設: 60)
    """
    fake = Faker()
    fake.add_provider(company)

    # Predefined list of coherent code messages and descriptions
    code_messages = [
        ("User authentication failed", "The system was unable to verify the user's credentials. This could be due to an incorrect username or password."),
        ("Database connection error", "The application failed to establish a connection with the database. This may be due to network issues or incorrect configuration."),
        ("File not found", "The requested file could not be located in the specified directory. Please check the file path and permissions."),
        ("Invalid input format", "The data provided does not match the expected format. Please review the input requirements and try again."),
        ("Session expired", "The user's session has timed out due to inactivity. Please log in again to continue."),
        ("Insufficient permissions", "The current user does not have the necessary rights to perform this action. Contact an administrator for assistance."),
        ("API rate limit exceeded", "The number of API requests has surpassed the allowed limit. Please wait before making additional requests."),
        ("Server overload", "The server is currently experiencing high traffic and cannot process the request. Try again later."),
        ("Data validation error", "One or more fields contain invalid data. Please review the form and correct any errors."),
        ("Payment processing failed", "The transaction could not be completed. Please check your payment information and try again."),
        ("Email delivery failed", "The system was unable to send the email. Verify the recipient's address and check your email configuration."),
        ("Unsupported browser", "Your current browser version is not supported. Please upgrade to a more recent version."),
    ]

    # 生成一組 unique codes
    codes = set()
    while len(codes) < len(code_messages):
        codes.add(fake.lexify(text="???-###", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    codes = list(codes)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['#', 'kind', 'res_code', 'code_msg', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for i in range(num_rows):
            code_msg, description = random.choice(code_messages)
            writer.writerow({
                '#': i + 1,
                'kind': fake.company(),
                'res_code': random.choice(codes),
                'code_msg': code_msg,
                'description': description
            })

def main():
    filename = input("Enter the filename for the test CSV (e.g., test_data.csv): ")
    num_rows = int(input("Enter the number of rows to generate (default is 60): ") or 60)
    
    generate_test_csv(filename, num_rows)
    print(f"Test CSV file '{filename}' has been generated with {num_rows} rows.")

if __name__ == "__main__":
    main()