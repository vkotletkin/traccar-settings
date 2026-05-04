import socket

data = bytes.fromhex("fd1c0000ce01012100004da91f004005d323b89aa30ea6ed070099fb0100f7fffdff0000942c4a88")
# fd1c0000e7010121000047aa1f004005d323b89aa30e9ced070093fb0100f8fffdff0000952c70ff
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(data, ("localhost", 5224))
print("Отправлено по UDP")
