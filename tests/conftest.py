from pytest import fixture

from config import Config


def pytest_addoption(parser):  # think of 'parser' is like a secret fixture provided - its the ~ argparse object
    parser.addoption(
        "--env", 
        action="store",
        help="Environment to run tests against"
    )


@fixture(scope='session')
def env(request):  # 'request' --- like a secret fixture again, to get some configurations (or something else) from pytest.
    # pytest --env=qa 
    # pytest --env qa
    # pytest --env="qa"
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg

