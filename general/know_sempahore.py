from threading import Semaphore, Thread
import time

# Max 3 connections allowed
db_connections = Semaphore(3)

def connect_to_database(connection_id):
    print(f"Connection {connection_id} is trying to connect to the database.")
    db_connections.acquire()
    print(f"Connection {connection_id} has connected to the database.")
    time.sleep(2)  # Simulate some database operations
    print(f"Connection {connection_id} is releasing the connection.")
    db_connections.release()

threads = [Thread(target=connect_to_database, args=(i,)) for i in range(5)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
# In this example, we create a semaphore with a maximum of 3 connections.
# We then create 5 threads that try to connect to the database.
# Only 3 of them will be able to connect at the same time, while the others will wait.
# This demonstrates how semaphores can be used to limit access to a resource.