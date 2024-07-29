import json

from pytest import fixture
from selenium import webdriver


data_path = 'test_data.json'

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)  # returns the data from json file (list/dict)
        return data

# any test that calls this fixture, will call the test for every parameter in the params;
# so you an have multiple test cases to call this params-- it's kinda global; so the param data is in one place, and not in every test case;
@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()

@fixture(params=load_test_data(data_path))
def tv_brand_from_fixture(request):
    data = request.param
    return data
