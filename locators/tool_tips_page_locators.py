class ToolTipsPageLocators:
    """
     <div class="tooltip-inner" bis_skin_checked="1">You hovered over the Button</div>
    <button id="toolTipButton" type="button" class="btn btn-success" aria-describedby="buttonToolTip">Hover me to see</button>
    """
    TOOL_TIPS_BTN = ("css selector", "button[id='toolTipButton']")
    HOVER_MSG = ("css selector", "div[class='tooltip-inner']")