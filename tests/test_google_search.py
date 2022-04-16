import pytest


@pytest.mark.parametrize("image_name", [ "image1", "image2", "image3"])
def test_google_search(locator, get_visit_result, check, image_name):
    locator.maximize_the_window
    check.take_screenshot(test=image_name)
    locator.click("Search", "cam_button")
    locator.wait(2)
    check.take_screenshot(test=image_name)
    locator.click("Search", "upload_image_tab")
    check.take_screenshot(test=image_name)
    locator.send_keys("Search", "choose_file_button",
                      f"/Users/cathy/Documents/Gitrep/google_search_UI_automation/data/{image_name}.jpeg")
    locator.wait(2)
    check.take_screenshot(test=image_name)
    possible_related_search = locator.get_text_value("Search_result", "possible_related_search")
    check.not_null(possible_related_search)
    related_search_list = possible_related_search.split(" ")
    print(related_search_list)
    check.list_not_empty(related_search_list)
    results_links = locator.elements("Search_result", "results_links")
    url = results_links[get_visit_result].get_attribute("href")
    locator.go_to(url)
    check.title_contains_words(locator.get_current_title(), related_search_list)
    check.result()
