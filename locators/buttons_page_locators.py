class ButtonsPageLocators:

    # CLICK_BTN_LOC = ('xpath', '//button[@class="btn btn-primary"](3)')
    CLICK_BTN_LOC = ('xpath', '//button[text()="Click Me"]')
    RIGHT_CLICK_BTN_LOC = ('xpath', '//button[@id="rightClickBtn"]')
    DOUBLE_CLICK_BTN_LOC = ('xpath', '//button[@id="doubleClickBtn"]')

    CLICK_TEXT_LOC = ('xpath', '//p[@id="dynamicClickMessage"]') #You have done a dynamic click
    RIGHT_CLICK_TEXT_LOC = ('xpath', '//p[@id="rightClickMessage"]') #You have done a right click
    DOUBLE_CLICK_TEXT_LOC = ('xpath', '//p[@id="doubleClickMessage"]') #You have done a double click