import server
import client
def main():
    s = server.Server()
    s.start()
    c = client.Client()
    c.sendMessage()

main()