import platform

from behave import fixture, use_fixture
from selenium import webdriver

from features.configs.cloud import CLOUD_URL
from features.configs.device import WUI_ADMIN_URL


@fixture(name="environment")
def environment(context):
    ext = '.exe' if platform.system() == 'Windows' else ''
    context.driver = webdriver.Chrome(executable_path=f'features/drivers/chromedriver{ext}')
    context.driver.maximize_window()
    context.wui_admin_url = WUI_ADMIN_URL
    context.cloud_url = CLOUD_URL
    yield context.driver, context.wui_admin_url, context.cloud_url
    context.driver.quit()


def before_all(context):
    use_fixture(environment, context)


# def before_tag(context, tag):
#     if tag == "fixture.environment":
#         use_fixture(environment, context)
