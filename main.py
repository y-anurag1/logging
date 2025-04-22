# main.py
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    logging.info("Script started.")
    try:
        x = 10 / 0
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        raise

if _name_ == "_main_":
    main()