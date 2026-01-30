title:::

on `rangin.front` (`arzhang3-front`),

```bash
@swallow \
	ethernet \
	test \
	- \
	--is_server 1 \
	--server_name 0.0.0.0
```

```text
⚙️ sudo -E /home/pi/venv/bluer_ai/bin/python3 -m bluer_ugv.swallow.session.classical.ethernet test --is_server 1 --server_name 0.0.0.0
🐬  bluer_ugv.swallow.session.classical.ethernet.testing.test: server_name=0.0.0.0, is_server=True, port=5050
🐬  EthernetClient created: host=0.0.0.0, port=5050, server.
🐬  press 5 to send a message.
🐬  EthernetClient: listening on 0.0.0.0:5050
⚠️  🐬  socket timeout.
⚠️  🐬  socket timeout.
🐬  EthernetClient: accepted ('192.168.0.140', 35742)
🐬  EthernetClient received EthernetCommand(hello)[{}]
🐬  EthernetClient.send: queue += EthernetCommand(hello)[{}]
🐬  EthernetClient: sent EthernetCommand(hello)[{}]
^C🐬  Ctrl+C, stopping.
🐬  EthernetClient._sock closed.
🐬  EthernetClient._listener closed.
```

on `rangin.top` (`rangin-top2`),

```bash
@swallow \
	ethernet \
	test \
	- \
	--is_server 0 \
	--server_name arzhang3-front.local
```

```text
⚙️ sudo -E /home/pi/venv/bluer_ai/bin/python3 -m bluer_ugv.swallow.session.classical.ethernet test --is_server 0 --server_name arzhang3-front.local
🐬  bluer_ugv.swallow.session.classical.ethernet.testing.test: server_name=arzhang3-front.local, is_server=False, port=5050
🐬  EthernetClient created: host=arzhang3-front.local, port=5050.
🐬  press 5 to send a message.
🐬  EthernetClient: connected to arzhang3-front.local:5050
🐬  EthernetClient.send: queue += EthernetCommand(hello)[{}]
🐬  EthernetClient: sent EthernetCommand(hello)[{}]
🐬  EthernetClient received EthernetCommand(hello)[{}]
^C🐬  Ctrl+C, stopping.
🐬  EthernetClient._sock closed.
```
