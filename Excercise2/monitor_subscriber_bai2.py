import paho.mqtt.client as mqtt
import json
BROKER = "localhost"
PORT = 1883
KEEPALIVE = 60 
TOPIC = "iot/lab/sensor01/data"

def on_connect(client,userdata,flags,reason_code,properties):
    if reason_code.is_failure:
        print("Kết nối thất bại")
        return
    client.subscribe(TOPIC,qos=1)
    print("Đang chờ dữ liệu từ sensor")

def on_message(client, userdata, message):
    PAYLOAD = json.loads(message.payload.decode("utf-8"))
    print(f"""Device: {PAYLOAD["device_id"]}
    Temperature: {PAYLOAD["temperature"]} C
    Humidity: {PAYLOAD["humidity"]} %
    """)
    if PAYLOAD["temperature"] > 35: print("====  CANH BAO: Nhiet do cao === \n\n")
    if PAYLOAD["humidity"] < 40: print("====  CANH BAO: Do am thap === \n\n")
def main():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER,PORT,KEEPALIVE)
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("Đang ngắt kết nối")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()