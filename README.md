<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>

<h2 align="center">
    ERP Platform – Quản lý Chấm công và Tiền lương
</h2>

<div align="center">
    <p align="center">
        <img src="docs/logo/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="docs/logo/fitdnu_logo.png" alt="FIT DNU Logo" width="180"/>
        <img src="docs/logo/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

</div>

## 📖 1. Giới thiệu

Hệ thống **ERP Platform – Quản lý Nhân sự, Chấm công và Tính lương** được xây dựng trong khuôn khổ học phần **Thực tập Doanh nghiệp** của sinh viên Khoa Công nghệ Thông tin – Đại học Đại Nam.

Hệ thống được phát triển dựa trên **nền tảng mã nguồn mở Odoo**, nhằm mô phỏng một hệ thống ERP thực tế trong doanh nghiệp, hỗ trợ các nghiệp vụ:

- Quản lý thông tin nhân sự
- Chấm công hàng ngày
- Tính lương theo tháng
- Quản lý hợp đồng, phòng ban, chức vụ

Thay vì xử lý thủ công hoặc rời rạc bằng Excel, hệ thống cung cấp một giải pháp **tập trung – tự động – dễ mở rộng**, phù hợp với môi trường doanh nghiệp vừa và nhỏ.

## 🔧 2. Các công nghệ được sử dụng

<div align="center">

### Hệ điều hành
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)

### Công nghệ chính
[![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](#)
[![XML](https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=codeforces&logoColor=white)](#)

### Database & Container
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

</div>

## 🚀 3. Hình ảnh các chức năng của hệ thống

### 👤 Quản lý Nhân sự

#### Trang quản lý nhân viên
<img width="1919" height="1071" alt="image" src="https://github.com/user-attachments/assets/66e22b9f-a436-4bad-88da-feda67552a38" />

#### Dashboard chấm công
<img width="1919" height="988" alt="image" src="https://github.com/user-attachments/assets/c9e8c34b-4b81-42cf-ac36-e8fa149c4f29" />

### ⏱️ Quản lý Chấm công

#### Trang quản lý chấm công
<img width="1917" height="986" alt="image" src="https://github.com/user-attachments/assets/4b7e3b2b-c4a4-444f-91a0-122685c7cb55" />

## ⚙️ 4. Cài đặt hệ thống

### 4.1. Cài đặt công cụ & môi trường

- **Ubuntu 22.04 (WSL2)**
- **Python 3.10**
- **Docker & Docker Compose**
- **Visual Studio Code**

Cài đặt các thư viện hệ thống cần thiết:

```bash
sudo apt-get update
sudo apt-get install -y \
libxml2-dev libxslt-dev libldap2-dev libsasl2-dev \
libssl-dev python3.10-dev python3.10-venv \
build-essential libffi-dev zlib1g-dev libpq-dev
````

### 4.2. Tải project

```bash
git clone (https://github.com/HiepV7413/TTDN-16-02-N3.git)
cd TTDN-16-02-N3
```

### 4.3. Khởi tạo môi trường ảo Python

```bash
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4.4. Setup Database bằng Docker

Chạy PostgreSQL bằng Docker Compose:

```bash
docker-compose up -d
```

Kiểm tra container:

```bash
docker ps
```

### 4.5. Cấu hình hệ thống Odoo

Tạo file `odoo.conf` (hoặc kế thừa từ `odoo.conf.template`):

```ini
[options]
addons_path = addons
db_host = localhost
db_user = odoo
db_password = odoo
db_port = 5431
xmlrpc_port = 8069
```

### 4.6. Chạy hệ thống

```bash
python3 odoo-bin.py -c odoo.conf -u all
```

Truy cập hệ thống tại:
👉 [http://localhost:8069](http://localhost:8069)

## 🔐 5. Đăng nhập lần đầu

* Khi truy cập lần đầu, tạo **database mới**
* Tạo tài khoản **Administrator**
* Cài đặt các module cần thiết của hệ thống

## 📝 6. Nguồn tham khảo

- Module chấm công  (Khóa 16):(https://github.com/HiepV7413/TTDN-16-02-N3.git)
# Ch-mc-ng-T-nh-L-ng
