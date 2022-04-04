# [TODO]: step 1
# Update the is_log_line function below to skip lines that are not valid log lines.
# Valid log lines have a timestamp, error type, and message. e.g. lines 1, 3, 7 and 37
# are all examples of lines (from sample.log) that would be filtered out. There will be
# no perfect way to do this just decide what you think is reasonable to get the test to
# pass. The only thing you are not allowed to do is filter out log lines based on the
# exact row numbers you want to remove.
def is_log_line(line):
    """Takes a log line and returns True if it is a valid log line and returns nothing
    if it is not.
    """
    return True


# [TODO]: step 2
# The generator should now return a dict that contains the keys "timestamp",
# "log_level", and "message". See the expected variable used in the test below to see
# what we expected to get as the first item from the generator.
def get_dict(line):
    """Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
    pass


# [TODO]: step 3
# Convert the timestamp value from its current format: DD/MM/YY HH:MM:SS to an ISO
# timestamp format: YYYY-MM-DD HH:MM:SS
def convert_to_iso(timestamp):
    pass


# YOU DON"T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == "__main__":
    # these are basic generators that will return
    # 1 line of the log file at a time
    def log_parser_step_1(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

    def log_parser_step_2(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield get_dict(line)

    def log_parser_step_3(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                d = get_dict(line)
                d["timestamp"] = convert_to_iso(d["timestamp"])
                yield d

    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE

    def test_step_1():
        with open("tests/step1.log") as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_step_1("sample.log"))

        if actual_out == test_lines:
            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w") as f:
                f.writelines(actual_out)

    def test_step_2():
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_step_2("sample.log"))

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    def test_step_3():
        expected_line2 = {
            "timestamp": "2021-11-03 08:51:01",
            "log_level": "INFO",
            "message": ":...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf",
        }
        lp = log_parser_step_3("sample.log")
        _ = next(lp)
        actual = next(lp)

        if expected_line2 == actual:
            print("STEP 3 SUCCESS")
        else:
            print(
                "STEP 3 FAILURE: your second item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected_line2}")
            print(f"Generator Output: {actual}")

            if expected_line2.get("log_level") == actual.get("log_level"):
                print("The log_level keys match")
            else:
                print("The log_level keys do not match")

            if expected_line2.get("timestamp") == actual.get("timestamp"):
                print("The timestamp keys match")
            else:
                print("The timestamp keys do not match")

            if expected_line2.get("message") == actual.get("message"):
                print("The message keys match")
            else:
                print("The message keys do not match")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")

    try:
        test_step_3()
    except Exception:
        print("step 3 test unable to run")
