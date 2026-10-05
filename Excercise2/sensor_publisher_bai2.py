import paho.mqtt.client as mqtt
import json, random,time
BROKER = "localhost"
KEEPALIVE = 60
PORT = 1883
TOPIC  = "iot/lab/sensor01/data" 
PAYLOAD = {
    "device_id": "",
    "temperature": 28.5,
    "humidity": 65.2
}

def send(client,sensor):   
    PAYLOAD["device_id"] = sensor
    PAYLOAD["temperature"] = round(random.randint(280,360)*0.1,2)
    PAYLOAD["humidity"] = round(random.randint(440 , 660)*0.1,2)
    result = client.publish(TOPIC, json.dumps(PAYLOAD), qos=1)
    result.wait_for_publish()
    print(f"{sensor} đã gửi dữ liệu thành công")
def main():
    client1 = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client1.connect(BROKER, PORT, KEEPALIVE)
    client1.loop_start()
    client2 = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client2.connect(BROKER, PORT, KEEPALIVE)
    client2.loop_start()
    try:
        while True:
            time.sleep(1.5)
            send(client1,"sensor01")
            time.sleep(1.5)
            send(client2,"sensor02")

    except KeyboardInterrupt :
        print("Đang ngắt kết nối")
    finally:
        client1.disconnect()
        client1.loop_stop()
        client2.disconnect()
        client2.loop_stop()


if __name__ == "__main__":
    main()
