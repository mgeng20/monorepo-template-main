class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    def add_message(self, message):
        self.messages.append(message)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._instance.messages = []
            print("Logger created exactly once")
        else:
            print("logger already created")

        return cls._instance


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger.instance()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
    main()
