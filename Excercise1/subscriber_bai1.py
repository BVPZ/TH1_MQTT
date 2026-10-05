import paho.mqtt.client as mqtt
from datetime import datetime
BROKER = "localhost"
PORT = 1883
KEEPALIVE = 60
TOPIC = "iot/lab/message"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Ket noi that bai: {reason_code}")
        return
    client.subscribe(TOPIC, qos=1)

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8", errors="replace")
    print("Nhan duoc message")
    print(f"Topic : {message.topic}")
    print(f"Payload : {payload}")
    print(f"Time : {datetime.now().strftime("%H:%M:%S")}")

def main():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, KEEPALIVE)
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("dang ngat ket noi...")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
