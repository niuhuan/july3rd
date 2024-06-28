import questionary

from .auto_fight import auto_fight


def j3_main():
    options_map = {"自动再次挑战": "1", "退出": "100"}
    option_ = questionary.select("选择", list(options_map.keys())).ask()
    if option_ is None:
        pass
    elif option_ == "自动再次挑战":
        auto_fight()
    pass
