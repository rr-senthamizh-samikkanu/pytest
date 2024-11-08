# need to install the below module since the module is one level higher up in parallel
# using the setup.py file and the command - `pip install .`
#  senth@Senthamizhs-MacBook-Air  ~/Documents/code/pytest/tests   unittesting1 ● ?  pip3 install .                     0|1 ↵  893  10:58:46
# ERROR: Directory '.' is not installable. Neither 'setup.py' nor 'pyproject.toml' found.

from custom_titlecase import title_case

class TitleCaseTests:
    def test_lower_text_is_uppercased_correctly(self):
        initial_text = 'this should be capitalized'
        expected_text = 'This Should Be Capitalized'
        returned_text = title_case(initial_text)
        assert returned_text == expected_text