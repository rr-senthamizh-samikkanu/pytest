import time


# pip -install pytest-xdist
# pytest -s-v -n4 (4 threads for n)
# if there's dependency on different tst, don't use this. only for isolated 100% tests
# -nauto (automatically detects)
def test_result_1_completes_as_expected():
    time.sleep(5)
    print("Result 1 has completed")

def test_result_2_completes_as_expected():
    time.sleep(5)
    print("Result 2 has completed")

def test_result_3_completes_as_expected():
    time.sleep(5)
    print("Result 3 has completed")

def test_result_4_completes_as_expected():
    time.sleep(5)
    print("Result 4 has completed")

def test_result_5_completes_as_expected():
    time.sleep(5)
    print("Result 5 has completed")

def test_result_6_completes_as_expected():
    time.sleep(5)
    print("Result 6 has completed")

def test_result_7_completes_as_expected():
    time.sleep(5)
    print("Result 7 has completed")

def test_result_8_completes_as_expected():
    time.sleep(5)
    print("Result 8 has completed")
