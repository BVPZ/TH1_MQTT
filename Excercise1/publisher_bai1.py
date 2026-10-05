import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
KEEPALIVE = 60
TOPIC = "iot/lab/message"


def main():
	client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
	client.connect(BROKER, PORT, KEEPALIVE)
	client.loop_start()

	try:
		while True:
			payload = input("Nhap payload (Ctrl+C de dung): ")
			result = client.publish(TOPIC, payload, qos=1)
			result.wait_for_publish()
			print(f"Da gui toi {TOPIC}: {payload}")
	except KeyboardInterrupt:
		print("\nDa nhan Ctrl+C, dang ngat ket noi...")
	finally:
		client.disconnect()
		client.loop_stop()


if __name__ == "__main__":
	main()