import allure
import logging
import pytest
import yaml


def getdate(filename) -> list:
    """
    获取yaml数据方法。
    输入：文件名
    输出：根据文件名来获取yaml文件中的参数数据，并返回一个list
    """
    try:
        with open(filename, "r", encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return data
    except:
        raise 'error'


class Test_del():

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.basetest
    @pytest.mark.run(order=4)
    @allure.feature('删除功能')
    @allure.story('删除一般场景')
    @pytest.mark.parametrize("name", getdate('../datas/del/delnormal_name.yaml'))
    def test_normal_del(self, objectget, name):
        logging.info(
            f'开始执行用例:删除英雄用例，hero_name:{name}')
        allure.dynamic.title(f'删除英雄用例，hero_name:{name}')
        with allure.step('测试步骤一，尝试删除英雄'):
            try:
                results = objectget.delete_hero(name)
                assert results is not False
            except AssertionError:
                logging.error(f'用例执行失败，原因是删除操作返回了False结果：删除英雄用例，hero_name:{name}')
                raise
        with allure.step('测试步骤二，断言测试结果'):
            try:
                for i in results:
                    assert i.get('name') is None
            except AssertionError:
                logging.error(
                    f'测试步骤二断言失败:由于添加英雄的name可重复，删除时并未删除所有同名英雄的字典从list中。'
                    f'导致assert判断结果是否删除干净时判断失误 hero_name:{name},字典{i},结果{results}')
                raise

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.advtest
    @pytest.mark.run(order=4)
    @allure.feature('删除功能')
    @allure.story('删除失败场景')
    @pytest.mark.parametrize("name", getdate('../datas/del/delraise_name.yaml'))
    def test_raise_del(self, objectget, name):
        logging.info(
            f'开始执行用例:删除英雄失败用例，hero_name:{name}')
        allure.dynamic.title(f'删除英雄失败用例，hero_name:{name}')
        with allure.step('测试步骤一，尝试删除英雄'):
            try:
                results = objectget.delete_hero(name)
            except:
                raise

        with allure.step('测试步骤二，断言结果'):
            try:
                assert results is False
            except AssertionError:
                logging.error(
                    f'测试步骤二断言失败,删除返回成功结果:hero_name:{name},结果{results}')
                raise

