import requests
import faker
import random
import string
import os
import time
from datetime import datetime
import pytz



# Fungsi untuk membersihkan layar
def clear_screen():
    if os.name == 'nt':  # Untuk Windows
        os.system('cls')
    else:  # Untuk Linux atau macOS
        os.system('clear')

# Membersihkan layar sebelum memulai script
clear_screen()

# Melanjutkan dengan kode lainnya...
# ...

# Menggunakan Faker untuk menghasilkan data acak
fake = faker.Faker()

# URL endpoint API
register_url = 'https://api.openloop.so/users/register'
login_url = 'https://api.openloop.so/users/login'

# Header untuk permintaan HTTP
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Bearer',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'chrome-extension://effapmdildnpkiaeghlkicpfflpiambm',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

# Fungsi untuk menghasilkan email acak
def generate_email():
    email_domains = ["@ab34.fr"]
    username = fake.user_name()[:15] + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{username}{random.choice(email_domains)}"

# Fungsi untuk menghasilkan password acak
def generate_password():
    return (
        random.choice(string.ascii_uppercase) +
        ''.join(random.choices(string.digits, k=3)) +
        '@' +
        ''.join(random.choices(string.ascii_lowercase, k=8)) +
        random.choice(string.ascii_uppercase)
    )

# Path ke file akun.txt dan token.txt
akun_file_path = os.path.join(os.path.dirname(__file__), 'akun.txt')
token_file_path = os.path.join(os.path.dirname(__file__), 'token.txt')

# Fungsi untuk registrasi pengguna baru
def register_user(register_data):
    return requests.post(register_url, json=register_data, headers=headers)

# Fungsi untuk login pengguna yang sudah terdaftar
def login_user(login_data):
    return requests.post(login_url, json=login_data, headers=headers)



#banner
banner = """
███████╗██╗  ██╗███████╗██╗███████╗      ██████╗  ██████╗ ███╗   ██╗███████╗
██╔════╝██║  ██║██╔════╝╚═╝██╔════╝     ██╔════╝ ██╔═══██╗████╗  ██║██╔════╝
███████╗███████║█████╗     ███████╗     ██║  ███╗██║   ██║██╔██╗ ██║█████╗  
╚════██║██╔══██║██╔══╝     ╚════██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝  
███████║██║  ██║███████╗   ███████║     ╚██████╔╝╚██████╔╝██║ ╚████║███████╗
╚══════╝╚═╝  ╚═╝╚══════╝   ╚══════╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝

                    Openloop.so Autoreff Python Version
"""
# Print banner
print(banner)

# Meminta input jumlah pengulangan dari pengguna
num_iterations = int(input("Masukkan jumlah akun: "))

# Meminta input invite_code dari pengguna
invite_code = input("Masukkan invite code: ")

# Ulangi proses registrasi dan login sesuai jumlah pengulangan yang dimasukkan pengguna
for i in range(num_iterations):
    # Generate email dan password
    generated_email = generate_email()
    username = generated_email.split('@')[0]  # Mengambil bagian depan dari email sebagai username
    password = generate_password()

    # Data yang akan dikirimkan dalam permintaan POST untuk registrasi
    register_data = {
        "name": username,  # Menggunakan bagian depan dari email sebagai nama
        "username": generated_email,
        "password": password,
        "inviteCode": invite_code
    }

    # Data yang akan dikirimkan dalam permintaan POST untuk login
    login_data = {
        "username": generated_email,
        "password": password
    }

    # Proses registrasi dan login
    register_response = register_user(register_data)
    if register_response.status_code == 200:
        current_time = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%H:%M:%S")
        print(f"\033[33m[{current_time}] - Status Registrasi - HTTP_CODE: {register_response.status_code} - {register_response.json()}\033[0m")

        login_response = login_user(login_data)
        if login_response.status_code == 200:
            current_time = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%H:%M:%S")
            print(f"\033[33m[{current_time}] - Proses login - HTTP_CODE: {login_response.status_code}\033[0m")
            login_data = login_response.json()
            access_token = login_data['data']['accessToken']
            
            # Simpan username, email, password, dan access token ke file akun.txt
            with open(akun_file_path, 'a') as akun_file:
                akun_file.write(f"Username: {username}, Email: {generated_email}, Password: {password}, AccessToken: {access_token}\n")

            # Simpan access token ke file token.txt
            with open(token_file_path, 'a') as token_file:
                token_file.write(f"{access_token}\n")

            #respon berhasil
            print(f"\033[32m[{current_time}] - Pembuatan Akun berhasil\033[0m")
            print(f"\033[32m[{current_time}] - Username: {username} - Email: {generated_email} - Password: {password}\033[0m")
            print(f"\033[32m[{current_time}] - AccessToken: {access_token}\033[0m")
        else:
            current_time = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%H:%M:%S")
            print(f"\033[31m[{current_time}] - Login failed with HTTP_CODE: {login_response.status_code}\033[0m")
            print(login_response.text)
    else:
        current_time = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%H:%M:%S")
        print(f"\033[31m[{current_time}] - Registration failed with HTTP_CODE: {register_response.status_code}\033[0m")
        print(register_response.text)
 #   time.sleep(1)  # Menambahkan jeda 1 detik antar iterasi
