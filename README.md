# ICMP Tunnel (`icmp-tunnel`)

**Category:** networking · **Difficulty:** medium · **Points:** 275

Flag blob fragments ride in ICMP echo payloads; reassemble and decode.

## Run it

```bash
docker build -t picoclone/icmp-tunnel .
# `picoclone start icmp-tunnel` (or the web UI) prints the docker run line with your
# PICOCLONE_SERVER + PICOCLONE_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is base64-encoded. Decode it to recover the flag.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
picoclone submit icmp-tunnel 'picoclone{...}'
```

## Hints

- Filter icmp in Wireshark and follow the data fields.
- Concatenate payloads and base64-decode.
