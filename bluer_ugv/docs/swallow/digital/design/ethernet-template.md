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
⚙️ python3 -m bluer_ugv.swallow.session.classical.ethernet test --is_server 1 --server_name 0.0.0.0
🐬  EthernetClient created: host=0.0.0.0, port=5050, server.
🐬  EthernetClient: listening on 0.0.0.0:5050
⚠️  🐬  socket timeout.
⚠️  🐬  socket timeout.
⚠️  🐬  socket timeout.
⚠️  🐬  socket timeout.
⚠️  🐬  socket timeout.
🐬  EthernetClient: accepted ('192.168.0.140', 49842)
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
⚙️ python3 -m bluer_ugv.swallow.session.classical.ethernet test --is_server 0 --server_name arzhang3-front.local
🐬  EthernetClient created: host=arzhang3-front.local, port=5050.
🐬  EthernetClient: connected to arzhang3-front.local:5050
```
