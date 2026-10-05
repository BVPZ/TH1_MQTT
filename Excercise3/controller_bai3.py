import paho.mqtt.client as mqtt
import json,time 

BROKER = "localhost"
PORT = 1883


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Ket noi that bai: {reason_code}")
        return

    client.subscribe("iot/lab/+/status", qos=1)


def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode("utf-8"))

    print("Trang thai nhan duoc:")
    print(json.dumps(payload, ensure_ascii=False))


def main():
    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2
    )

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT)
    client.loop_start()

    try:
        while True:
            device = input("Nhap ten thiet bi: ")
            if device not in ["light01","fan01","pump01"]:
                print("Ten thiet bi ko hop le")
                continue
            if device.upper() == "EXIT":
                break

            status = input("Nhap trang thai: ").upper()

            if status not in ["ON", "OFF"]:
                print("Trang thai khong hop le!")
                continue

            topic = f"iot/lab/{device}/cmd"

            payload = {
                "device_id": device,
                "status": status
            }

            client.publish(topic, json.dumps(payload), qos=1)

            print(f"Da gui lenh {status} toi {device}")
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()