# TH1_MQTT - Hướng dẫn chạy 3 bài thực hành MQTT

BROKER sử dụng trong bài thực hành là `localhost`, chạy trực tiếp trên máy cá nhân.

## 1. Môi trường trước khi chạy các bài thực hành

- Python 3.x
- Thư viện `paho-mqtt`
- Cấu hình MQTT broker
- Một IDE hoặc VS Code

Các lệnh cần chạy trên terminal:

```bash
pip install paho-mqtt
```

Sau đó chạy tiếp:

```bash
mosquitto -v
```

Lệnh này giúp mở cổng `1883` trên `localhost`, để các client MQTT có thể kết nối với broker.

## 2. Thực hiện bài 1: Ứng dụng gửi và nhận thông điệp MQTT cơ bản

### Bước thực hiện

- Trong thư mục `Excercise1`, chạy file `publisher_bai1.py` trên 1 terminal.
- Tiếp theo chạy file `subscriber_bai1.py` trong 1 terminal khác.
- Quay lại terminal ban đầu và nhập `message` bất kì để gửi cho client bên phía `subscriber` đọc.
- Quan sát bên phía terminal của `subscriber` đã nhận được dữ liệu chưa.
- Có thể quay lại terminal ban đầu và tiếp tục gửi `message`.

### Ví dụ chạy

Terminal 1:
```bash
cd Excercise1
python publisher_bai1.py
```

Terminal 2:
```bash
cd Excercise1
python subscriber_bai1.py
```

Sau đó ở terminal publisher nhập:
```text
hello MQTT
```

### Kết quả bài 1

- Bên publisher đã gửi được dữ liệu nhiều lần lên broker.
- Bên subscriber nhận được dữ liệu từ broker và in ra kết quả gồm `TOPIC`, `PAYLOAD`, và thời gian nhận.

Ví dụ đầu ra bên subscriber:
```text
Nhan duoc message
Topic : iot/lab/message
Payload : hello MQTT
Time : 14:20:30
```

## 3. Thực hiện bài 2:Mô phỏng cảm biến nhiệt độ và độ ẩm bằng MQTT

### Bước thực hiện

- Trong thư mục `Excercise2`, chạy file `sensor_publisher_bai2.py` trên 1 terminal.
- Tiếp theo chạy file `monitor_subscriber_bai2.py` trên 1 terminal khác.
- Chương trình publisher sẽ tự động gửi dữ liệu cảm biến lên topic MQTT.
- Bên subscriber đọc dữ liệu JSON và hiển thị thông tin như `device_id`, `temperature`, `humidity`.
- Nếu nhiệt độ hoặc độ ẩm vượt ngưỡng cảnh báo, chương trình sẽ hiển thị cảnh báo tương ứng.

### Ví dụ chạy

Terminal 1:
```bash
cd Excercise2
python sensor_publisher_bai2.py
```

Terminal 2:
```bash
cd Excercise2
python monitor_subscriber_bai2.py
```

### Kết quả bài 2

- Bên sensor publisher đã gửi dữ liệu cảm biến liên tục lên broker.
- Bên monitor subscriber đã nhận dữ liệu từ broker và hiển thị thông tin nhiệt độ, độ ẩm và trạng thái cảnh báo.
- Nếu `temperature > 35` thì in cảnh báo `Nhiệt độ cao`.
- Nếu `humidity < 40` thì in cảnh báo `Độ ẩm thấp`.

Ví dụ đầu ra:
```text
Device: sensor01
Temperature: 35.8 C
Humidity: 54.2 %
==== CANH BAO: Nhiet do cao ===
```

## 4. Thực hiện bài 3:Mô phỏng hệ thống điều khiển đèn thông minh qua MQTT

### Bước thực hiện

- Trong thư mục `Excercise3`, chạy file `device_bai3.py` trên 1 terminal.
- Tiếp theo chạy file `controller_bai3.py` trên 1 terminal khác.
- Ở terminal controller, nhập tên thiết bị và trạng thái điều khiển.
- Ví dụ: `fan01` và `ON`.
- Thiết bị nhận lệnh và trả về trạng thái của thiết bị lên broker.
- Controller sẽ nhận lại dữ liệu phản hồi từ thiết bị và hiển thị trên màn hình.

### Ví dụ chạy

Terminal 1:
```bash
cd Excercise3
python device_bai3.py
```

Terminal 2:
```bash
cd Excercise3
python controller_bai3.py
```

Giao diện nhập dữ liệu trên controller:
```text
Nhap ten thiet bi: fan01
Nhap trang thai: ON
```

### Kết quả bài 3

- Thiết bị nhận được lệnh điều khiển từ controller thông qua topic MQTT.
- Thiết bị phản hồi trạng thái lên broker.
- Controller nhận được phản hồi và in ra trạng thái hiện tại của thiết bị.

Ví dụ đầu ra:
```text
Da gui lenh ON toi fan01
Trang thai nhan duoc:
{"device_id": "fan01", "status": "ON"}
```

## 5. Kết luận chung

Ba bài thực hành trên minh họa rõ cách giao tiếp MQTT theo mô hình publish/subscribe:

- Bài 1: gửi và nhận message đơn giản
- Bài 2: thu thập và cảnh báo dữ liệu cảm biến
- Bài 3: điều khiển thiết bị và phản hồi trạng thái

Nhờ có broker MQTT chạy trên `localhost`, các client Python có thể trao đổi dữ liệu nhanh chóng và dễ dàng trong môi trường máy tính cá nhân.

## 6. Tổng kết

- Dự án đã hoàn thành 3 bài thực hành MQTT cơ bản.
- Publisher/subscriber hoạt động đúng theo mô hình truyền tin.
- Sensor/monitor có thể theo dõi dữ liệu thời gian thực.
- Controller/device có thể gửi lệnh và nhận phản hồi trạng thái.
- Đây là nền tảng để phát triển các ứng dụng IoT phức tạp hơn trong tương lai.
