class Web:
    def __get(self, url):
        return self.driver.get(url)

    def __click(self, locator: list):
        # by = list(locator.keys())[0]
        # value = list(locator.values())[0]
        by = locator[0]
        value = locator[1]
        return self.driver.find_element(by, value).click()

    def __send_keys(self, params: list):
        by = params[0]
        value = params[1]
        content = params[2]

        return self.driver.find_element(by, value).send_keys(content)

    def run_step(self, step: dict):
        for key, value in step.items():
            if key == "打开浏览器":
                self.driver = eval(f"webdriver.{value}()")
                break
            elif key == '访问':
                self.__get(value)
                break
            elif key == '点击':
                self.__click(value)
                break
            elif key == '输入':
                self.__send_keys(value)
                break
            elif key == '断言':
                assert eval(value)
                break
            elif key == '关闭浏览器':
                self.driver.quit()
                break
        else:
            return False
        return True


# 将对象初始化
web: Web = None
