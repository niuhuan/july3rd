from tasks.game.starrailcontroller import StarRailController
from module.config import cfg
from module.logger import log
import time
from module.automation import auto

def auto_fight():
        game = StarRailController(cfg.game_path, cfg.game_process_name, cfg.game_title_name, 'UnityWndClass', log)
        game.switch_to_game()
        game.check_resolution(1920, 1080)
        i = 1
        while True:
             wait_fight(i)
             i = i+1
             auto.click_element("./assets/images/zh_CN/fight/fight_again.png", "image", 0.9)      


def wait_fight(num, timeout=1800):
    log.info("进入战斗")
    time.sleep(5)

    start_time = time.time()
    while time.time() - start_time < timeout:
        if auto.find_element("./assets/images/zh_CN/fight/fight_again.png", "image", 0.9):
            log.info("战斗完成")
            log.info(f"第{num}次副本完成")
            return True
        elif cfg.auto_battle_detect_enable and auto.find_element("./assets/images/share/base/not_auto.png", "image", 0.9, crop=(0.0 / 1920, 903.0 / 1080, 144.0 / 1920, 120.0 / 1080)):
            log.info("尝试开启自动战斗")
            auto.press_key("v")

        time.sleep(2)

    log.error("战斗超时")
    raise RuntimeError("战斗超时")
