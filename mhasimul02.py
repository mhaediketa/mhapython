# Import required libraries
import time
import datetime
import numpy as np
import pandas as pd


# Define the customer class (i.e., the agent)
from IPython.core.display import display


class customer:
    def __init__(self):
        self.customer_number = 0
        self.time_arrived_to_system = 0
        self.time_arrived_to_queue = 0
        self.time_start_order_placing = 0
        self.time_end_order_placing = 0
        self.time_order_delivered = 0
        self.time_exit_system = 0
        self.total_time_placing_order = 0
        self.total_time_waiting_for_order = 0


# Initialize lists where we will store the information for future analysis
customer_number_list = []
time_arrived_to_system_list = []
time_arrived_to_queue_list = []
time_start_order_placing_list = []
time_end_order_placing_list = []
time_order_delivered_list = []
time_exit_system_list = []
total_time_placing_order_list = []
total_time_waiting_for_order = []

# Initialize customers count
customer_number = 0

# Define the model running time
model_run_time = 30

# Set model initial running time
initial_time = time.time()

# Run simulation model
while time.time() < initial_time + model_run_time:
    # New customer instantiation
    new_customer = customer()
    new_customer.customer_number = customer_number + 1
    customer_number_list.append(new_customer.customer_number)

    # Customer arrives to system
    new_customer.time_arrived_to_system = time.time()
    time_arrived_to_system_list.append(
        datetime.datetime.fromtimestamp(new_customer.time_arrived_to_system).strftime('%m/%d/%Y, %H:%M:%S'))

    # Customer walks to queue
    time.sleep(np.random.triangular(1, 2, 3))

    # Customer arrives to queue
    new_customer.time_arrived_to_queue = time.time()
    time_arrived_to_queue_list.append(
        datetime.datetime.fromtimestamp(new_customer.time_arrived_to_queue).strftime('%m/%d/%Y, %H:%M:%S'))

    # Customer waiting time on queue
    time.sleep(np.random.triangular(2, 3, 4))

    # Customer arrives to order point and starts placing order
    new_customer.time_start_order_placing = time.time()
    time_start_order_placing_list.append(
        datetime.datetime.fromtimestamp(new_customer.time_start_order_placing).strftime('%m/%d/%Y, %H:%M:%S'))

    # Time order being taken
    time.sleep(np.random.triangular(1, 2, 3))

    # Customer ends placing order
    new_customer.time_end_order_placing = time.time()
    time_end_order_placing_list.append(
        datetime.datetime.fromtimestamp(new_customer.time_end_order_placing).strftime('%m/%d/%Y, %H:%M:%S'))

    # Total time spent for placing the order
    new_customer.total_time_placing_order = new_customer.time_end_order_placing - new_customer.time_start_order_placing
    total_time_placing_order_list.append(new_customer.total_time_placing_order)

    # Time order being processed
    time.sleep(np.random.triangular(4, 5, 6))

    # Customer recevies order
    new_customer.time_order_delivered = time.time()
    time_order_delivered_list.append(
        datetime.datetime.fromtimestamp(new_customer.time_order_delivered).strftime('%m/%d/%Y, %H:%M:%S'))

    # Total time customer waited for the order to be recevied
    new_customer.total_time_waiting_for_order = new_customer.time_order_delivered - new_customer.time_end_order_placing
    total_time_waiting_for_order.append(new_customer.total_time_waiting_for_order)

    # Time customer spends validating order
    time.sleep(np.random.triangular(1, 2, 3))

    # Customer exists order
    new_customer.time_exit_system = time.time()
    time_exit_system_list.append(
        datetime.datetime.fromtimestamp(new_customer.time_exit_system).strftime('%m/%d/%Y, %H:%M:%S'))

    customer_number += 1

# Create data frame with
df = pd.DataFrame(
    {
        "customer_number": customer_number_list,
        "time_arrived_to_system": time_arrived_to_system_list,
        "time_arrived_to_queue": time_arrived_to_queue_list,
        "time_start_order_placing": time_start_order_placing_list,
        "time_end_order_placing": time_end_order_placing_list,
        "time_order_delivered": time_order_delivered_list,
        "time_exit_system": time_exit_system_list,
        "time_placing_order": total_time_placing_order_list,
        "time_waiting_for_order": total_time_waiting_for_order
    }
)

# Set the customer number column as the index
df.set_index("customer_number", inplace=True)

# Display dataframe top rows
display(df.head())

# Display smmary statistics
display(df[["time_placing_order", "time_waiting_for_order"]].describe())
