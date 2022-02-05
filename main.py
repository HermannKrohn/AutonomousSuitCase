def setup():
    pass


def loop():
    pass


def cleanup():
    pass


def main():
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()


if __name__ == "__main__":
    main()
