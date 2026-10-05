import paho.mqtt.client as mqtt
import json
BROKER = "localhost"
PORT = 1883

def publish_status(client:mqtt.Client,device,status):
    TOPIC = f"iot/lab/{device}/status"
    PAYLOAD = {
      "device_id": device,
      "status": status
    }
    client.publish(TOPIC,json.dumps(PAYLOAD),1)
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Ket noi that bai: {reason_code}")
        return
    client.subscribe("iot/lab/+/cmd", qos=1)
    
def on_message(client, userdata, message):
    PAYLOAD = json.loads(message.payload.decode("utf-8"))
    device = PAYLOAD["device_id"]
    status = PAYLOAD["status"]
    publish_status(client,device,status)

def main():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER,PORT)
    client.loop_start()
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("Đang ngắt kết nối")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()