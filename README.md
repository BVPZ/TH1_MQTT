BROKER sử dụng trong bài thực hành là localhost, chạy trực tiếp trên máy cá nhân

Môi trường trước khi chạy các bài thực hành:
 - Python 3.x
 - Thư viện paho-mqtt
 - Cấu hình MQTT broker
 - Một IDE hoặc VS Code
 - trong terminal chạy lệnh "pip install paho-mqtt"
sau đó chạy tiếp "mosquitto -v" để mở cổng 1883 trên localhost

Thực hiện bài 1:
 - Trong thư mục Excercise1 chạy file publisher_bai1.py trên 1 terminal
 - Tiếp theo chạy file subsciber_bai1.py trong 1 terminal khác
 - Quay lại terminal ban đầu và nhập message bất kì để gửi cho client bên phía subsciber đọc
 - Quan sát bên phía terminal của subsciber đã nhận được dữ liệu chưa
 - Có thể quay lại terminal ban đầu và tiếp tục gửi message

Kết quả bài 1:
 - Bên publisher đã gửi được dữ liệu nhiều lần lên broker
 - Bên subsciber nhận được dữ liệu từ broker và in ra kết quả gồm TOPIC, PAYLOAD, và thời gian nhận
 
