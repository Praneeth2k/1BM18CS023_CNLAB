def main():
    rate = int(input("Enter the output rate (bytes/sec): "))
    buffer_size = int(input("Enter the buffer size: "))

    n = int(input("Enter the number of packets to be sent: "))
    print("Enter the sizes of the packets in bytes")
    packets = []
    for i in range(n):
        packets.append(int(input()))
    buffer_storage = 0
    for i in range(len(packets)):
        print("Packet no", i, " size:", packets[i])
        availableSpaceInBuffer = buffer_size - buffer_storage

        if(packets[i] > availableSpaceInBuffer):
            print("Bucket overflow")
            break
        else:
            buffer_storage +=packets[i]
            to_send = min(rate, buffer_storage)
            print("Bucket output successful")
            print("Last", to_send, "bytes sent")
            buffer_storage -= to_send
main()