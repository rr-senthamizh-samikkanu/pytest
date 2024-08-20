from pytest import mark

# parametrize: it's a specail mark keyword; unlike 'smoke,' 'ui' which are custom marks.
# for every parameter, the test runs that many times
# here we are coupling the data with the test though; there's a better way; -- via fixture (see: tv_brand_from_fixture test case)
@mark.parametrize('tv_brand', [
        ('Samsung'), # reason for tuple is we can send in multiple attributes if needed
        ('Sony'),
        ('Vizio')
    ]
)
# @mark.skip
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")

def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://techstepacademy.com/training-ground')

def test_television_turns_on_from_fixture(tv_brand_from_fixture):
    print(f"{tv_brand_from_fixture} turns on as expected")
