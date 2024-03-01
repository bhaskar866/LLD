import re
import threading

class MessageQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()

    def enqueue(self, message):
        with self.lock:
            self.queue.append(message)

    def dequeue(self):
        with self.lock:
            if len(self.queue) > 0:
                return self.queue.pop(0)
            return None

class Publisher:
    def __init__(self, queue):
        self.queue = queue

    def publish(self, message):
        self.queue.enqueue(message)

class Subscriber:
    def __init__(self, pattern, callback):
        self.pattern = pattern
        self.callback = callback
        self.dependencies = []
        self.processed_messages = []

    def add_dependency(self, subscriber):
        self.dependencies.append(subscriber)

    def notify(self, message):
        # if re.match(self.pattern, message):
        self.callback(message)
        self.processed_messages.append(message)

    def has_processed(self, message):
        return message in self.processed_messages

class SubscriptionManager:
    def __init__(self):
        self.subscribers = []

    def register(self, subscriber):
        self.subscribers.append(subscriber)

    def deregister(self, subscriber):
        self.subscribers.remove(subscriber)

    def get_subscribers(self):
        return self.subscribers

class MessageDispatcher:
    def __init__(self, queue, subscription_manager):
        self.queue = queue
        self.subscription_manager = subscription_manager
        self.dispatch_thread = threading.Thread(target=self.start_dispatching)
        self.dispatch_thread.daemon = True

    def start(self):
        self.dispatch_thread.start()

    def join(self):
        self.dispatch_thread.join()

    def start_dispatching(self):
        while self.queue:
            message = self.queue.dequeue()
            if message:
                self.dispatch(message)

    def dispatch(self, message):
        for subscriber in self.subscription_manager.get_subscribers():
            if self.can_process(subscriber, message):
                try:
                    subscriber.notify(message)
                except Exception as e:
                    # Implement retry logic here
                    print(f"Error processing message {message}: {e}")

    def can_process(self, subscriber, message):
        return all(dependency.has_processed(message) for dependency in subscriber.dependencies)

# Example usage
if __name__ == "__main__":
    queue = MessageQueue()
    manager = SubscriptionManager()
    dispatcher = MessageDispatcher(queue, manager)
    dispatcher.start()
    

    

    def callback(message):
        print(f"Received message: {message}")

    subscriber1 = Subscriber(".*Hello.*", callback)
    subscriber2 = Subscriber(".*world.*", callback)

    subscriber1.add_dependency(subscriber2)
    # subscriber2.add_dependency(subscriber1)

    manager.register(subscriber1)
    manager.register(subscriber2)

    publisher = Publisher(queue)
    publisher.publish('{"message": "Hello, world!"}')
    publisher.publish('{"message": "Another message"}')

    dispatcher.join()