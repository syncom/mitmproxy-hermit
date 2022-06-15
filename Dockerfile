FROM ubuntu
RUN apt update && apt upgrade -y && apt install ca-certificates curl git -y
WORKDIR /root
COPY mitmproxy-ca-cert.cer /usr/local/share/ca-certificates/mitmproxy.crt
RUN update-ca-certificates
