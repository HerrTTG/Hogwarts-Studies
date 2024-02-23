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

class Test_update():
    '''
    发现问题：更新也是只更新遍历到的第一个符合条件的字典，由于name没做去重校验。
    存在多个同名的英雄字典。但更新只能更新遍历到的第一个。
    '''

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.basetest
    @pytest.mark.run(order=3)
    @allure.feature('更新功能')
    @allure.story('更新一般场景')
    @pytest.mark.parametrize("volume", getdate('../datas/update/updatenormal_volume.yaml'))
    @pytest.mark.parametrize("name", getdate('../datas/update/updatenormal_name.yaml'))
    def test_normal_update(self, objectget, name, volume):
        # 这里的volume是修改后的值
        logging.info(f'开始执行用例:更新英雄用例，hero_name:{name} voluem:{volume}')
        allure.dynamic.title(f'更新英雄用例，hero_name:{name} voluem:{volume}')
        with allure.step('测试步骤一,尝试更新英雄'):
            try:
                result = objectget.update_hero(name, volume)
                assert result
            except AssertionError:
                logging.error(f'更新失败，结果返回false:更新英雄用例，hero_name:{name} voluem:{volume}')
                raise
            except:
                logging.error(f'更新失败:更新英雄用例，hero_name:{name} voluem:{volume}')
        with allure.step('测试步骤二,断言更新结果'):
            try:
                assert result["name"] == name and result["volume"] == volume
            except AssertionError:
                raise

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.advtest
    @pytest.mark.run(order=3)
    @allure.feature('更新功能')
    @allure.story('更新失败场景')
    @pytest.mark.parametrize("volume", getdate('../datas/update/updateraise_volume.yaml'))
    @pytest.mark.parametrize("name", getdate('../datas/update/updateraise_name.yaml'))
    def test_raise_update(self, objectget, name, volume):
        # 这里的volume是修改后的值
        logging.info(f'开始执行用例:更新英雄失败用例，hero_name:{name} voluem:{volume}')
        allure.dynamic.title(f'更新英雄失败用例，hero_name:{name} voluem:{volume}')
        with allure.step('测试步骤一,尝试更新英雄'):
            try:
                result = objectget.update_hero(name, volume)
            except:
                logging.error(f'更新失败:更新英雄用例，hero_name:{name} voluem:{volume}')
        with allure.step('测试步骤二,断言更新结果'):
            try:
                assert result is False
            except AssertionError:
                if isinstance(volume, float) or volume <= 0 or volume >= 100:
                    logging.error(
                        f'更新失败，结果为True,且volume超出需求所要求的1-99:更新英雄用例，hero_name:{name} voluem:{volume}'
                        f'发现问题：创建英雄时要求血量在1-99，但更新时无任何输入校验，超出范围的也可成功'
                        f'发现问题：创建英雄时要求血量为正整数，但更新时无任何输入校验，浮点数也可成功')
                    raise
                else:
                    logging.info(f'更新成功用例，hero_name:{name} 找得到，且 voluem:{volume} 符合需求范围要求')
                    pass
