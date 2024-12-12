import pydivert
import time

def set_speed_limit(rate_kbps):
    """
    Limit the download speed by delaying packets.

    :param rate_kbps: Speed limit in kilobits per second.
    """
    bytes_per_second = (rate_kbps * 1000) // 8
    delay = 0.1  # 100ms delay per loop
    max_bytes_per_delay = bytes_per_second * delay

    print(f"Applying speed limit: {rate_kbps} kbps")

    with pydivert.WinDivert("inbound") as w:
        w.open()
        buffer = []
        buffer_size = 0

        for packet in w:
            buffer.append(packet)
            buffer_size += len(packet.raw)

            if buffer_size >= max_bytes_per_delay:
                time.sleep(delay)
                while buffer:
                    w.send(buffer.pop(0))
                buffer_size = 0

def remove_speed_limit():
    """
    Stop filtering packets, effectively removing the speed limit.
    """
    print("Speed limit removed. Restarting unfiltered traffic.")

if __name__ == "__main__":
    print("--- Internet Speed Limiter (Windows) ---")
    print("1. Set Speed Limit")
    print("2. Remove Speed Limit")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        rate = int(input("Enter the speed limit in kbps (e.g., 1000 for 1Mbps): "))
        try:
            set_speed_limit(rate)
        except KeyboardInterrupt:
            print("\nSpeed limiting interrupted by user.")
    elif choice == "2":
        remove_speed_limit()
    else:
        print("Invalid choice. Exiting.")
