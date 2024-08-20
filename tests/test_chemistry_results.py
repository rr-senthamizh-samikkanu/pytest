import time


# pip install pytest-xdist or # pip3 install pytest-xdist
# if you don't have this package, you'll get the below error
# ERROR: usage: pytest [options] [file_or_dir] [file_or_dir] [...]
# pytest: error: unrecognized arguments: -n4
#   inifile: None
#   rootdir: /Users/senth/Documents/code/pytest


# pytest -s-v -n4 (4 threads for n)
# pytest -s-v -nauto
# if there's dependency on different tests (or database state), don't use this. only for isolated 100% tests
# -nauto (automatically detects)

# I/O bound problems - where we are waiting on something -- multiple threads in one process should do for paralleism (concurrent)
# global interpreter lock (gil) - let you run only one job per process (->\\-> ... hops arounds the tests when idle 
# - waiting on API response, network delay, website response etc)
# more like you working on mulitple jira in one sprint (hopping between different jiras)

# CPU bound probles - where the slowness due to computation/complexity -- multiple processes for parallelism (concurrent and parallel)
# see screenshots in this folder for the it.
# all tests runs in differentt process (each on their own CPU cores) - no shared memory (almost) - no hopping arounds
# each having their own gil
# complex math calcualtions/loops, big data ...etc 

#xdist -- open prcess if it can, if there's none more, then it opens threads

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
