import server
import client

def main():
    s = server.Server()
    s.start()
    c = client.Client()
    c.sendMessage()

if __name__ == "__main__":
    main()