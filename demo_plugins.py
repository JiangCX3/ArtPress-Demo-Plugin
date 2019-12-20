import artpress_api


class View:
    def __init__(self):
        PanelMenu = (
            ["To Baidu", artpress_api.JunpTo.url("www.baidu.com")],
            ["Demo Options", artpress_api.JunpTo.plugins_options()],
        )

    def adminPage(self):
        return {
            "template_data": {"Demo": 123},
        }
