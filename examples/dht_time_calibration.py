# SPDX-FileCopyrightText: 2021 yeyeto2788 for Adafruit Industries
# SPDX-License-Identifier: MIT

import json
import time

import board

import adafruit_dht

pin_to_use = "PG6"

# Maximum number of tries per timing
max_retries_per_time = 10
# Minimum time from where to start testing
min_time = 500
# Maximum time on where to stop testing
max_time = 2000
# Increment on time
time_increment = 100

# Variable to store all reads on a try
reads = {}

print("\nInitializing test.\n", f"Total tries per trig_wait {max_retries_per_time}")

for milliseconds in range(min_time, max_time, time_increment):
    # Instantiate the DHT11 object.
    dhtDevice = adafruit_dht.DHT11(pin=getattr(board, pin_to_use))
    # Change the default wait time for triggering the read.
    # pylint: disable=W0212
    dhtDevice._trig_wait = milliseconds

    # pylint: disable=W0212
    print(f"Using 'trig_wait' of {dhtDevice._trig_wait}")
    # Reset the read count for next loop
    reads_count = 0

    # Create the key on the reads dictionary with the milliseconds used on
    # this try.
    if milliseconds not in reads:
        reads[milliseconds] = {"total_reads": 0}

    for try_number in range(0, max_retries_per_time):
        try:
            # Read temperature and humidity
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity
            read_values = {"temperature": temperature, "humidity": humidity}

            if try_number not in reads[milliseconds]:
                reads[milliseconds][try_number] = read_values

            reads_count += 1
        except RuntimeError as e:
            time.sleep(2)
        else:
            time.sleep(1)

    reads[milliseconds]["total_reads"] = reads_count

    print(f"Total read(s): {reads[milliseconds]['total_reads']}\n")
    dhtDevice.exit()

# Gather the highest read numbers from all reads done.
best_result = max([reads[milliseconds]["total_reads"] for milliseconds in reads])

# Gather best time(s) in milliseconds where we got more reads
best_times = [
    milliseconds
    for milliseconds in reads
    if reads[milliseconds]["total_reads"] == best_result
]
print(
    f"Maximum reads: {best_result}  out of {max_retries_per_time} with the "
    f"following times: {', '.join([str(t) for t in best_times])}"
)

# change the value on the line below to see all reads performed.
print_all = False
if print_all:
    print(json.dumps(reads))
