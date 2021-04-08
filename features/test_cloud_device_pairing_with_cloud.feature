@fixture.environment
Feature: Showing off behave

  Scenario: Run a simple test

    When I open avstudio page in wui admin
    When I get pairing code from cloud page
    When I open login page in Cloud
    When login to Cloud with username and password
    When I click btn Pair device
    When I pair device by MyFavoriteDevice name and code

#    with allure.step("6. Validate that the device has expected name"):
#        DevicePageHelper(driver_chrome).validate_device_name(device_name)
#
#    with allure.step("7. Unpair the device"):
#        driver_chrome.get(WUI_ADMIN_URL + "/avstudio")
#        EpiphanCloudPageHelper(driver_chrome).unpair_device()
