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


class Test_add():
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.basetest
    @pytest.mark.run(order=1)
    @allure.feature('添加功能')
    @allure.story('添加一般场景')
    @pytest.mark.parametrize("power", getdate('../datas/add/addnormal_power.yaml'))
    @pytest.mark.parametrize("volume", getdate('../datas/add/addnormal_volume.yaml'))
    @pytest.mark.parametrize("name", getdate('../datas/add/addnormal_name.yaml'))
    def test_normal_add(self, objectget, name, volume, power):
        '''
        发现问题：name可重复 同名英雄可重复添加到list中
        '''
        logging.info(f'开始执行用例:添加英雄用例，hero_name:{name} hero_volume:{volume} hero_power:{power}')
        allure.dynamic.title(f'添加英雄用例，hero_name:{name} hero_volume:{volume} hero_power:{power}')
        with allure.step('测试步骤一,尝试新增英雄'):
            try:
                results = objectget.create_hero(name, volume, power)
            except:
                logging.error(f'测试步骤一失败:添加英雄用例，hero_name:{name} hero_volume:{volume} hero_power:{power}')
                raise
        with allure.step('测试步骤二,断言返回结果'):
            try:
                assert results is True
            except AssertionError:
                logging.error(
                    f'测试步骤二断言结果不正确:添加英雄用例，hero_name:{name} hero_volume:{volume} hero_power:{power}')
                raise

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.advtest
    @allure.feature('添加功能')
    @allure.story('添加非正确输入的失败场景')
    @pytest.mark.parametrize("power", getdate('../datas/add/addraise_power.yaml'))
    @pytest.mark.parametrize("volume", getdate('../datas/add/addraise_volume.yaml'))
    @pytest.mark.parametrize("name", getdate('../datas/add/addraise_name.yaml'))
    def test_raise(self, name, volume, power, objectget):
        '''
        发现问题 新增英雄时如果传参为null可以正常添加
                新增英雄血量和共计林并非只支持正整数,可以使用浮点数
        '''
        logging.info(
            f'开始执行用例:添加英雄非正确输入失败用例，hero_name:{name} hero_volume:{volume} hero_power:{power}')
        allure.dynamic.title(f'添加英雄非正确输入失败用例，hero_name:{name} hero_volume:{volume} hero_power:{power}')
        with allure.step('用例步骤一，尝试添加英雄。'):
            try:
                results = objectget.create_hero(name, volume, power)
            except TypeError:
                pass
            except:
                logging.error(
                    f'测试步骤一失败:添加英雄非正确输入失败用例，hero_name:{name} hero_volume:{volume} hero_power:{power}')
                raise

        # 过滤因为笛卡尔积生成的交叉数据组合为符合正确输入的用例
        # 过滤非正整数的输入值
        if (isinstance(volume, int) and isinstance(power, int)
                and 0 < volume < 100 and power > 0 and name is not None):
            pass
        else:
            with allure.step('用例步骤二，断言结果为失败。'):
                try:
                    assert results is False
                except UnboundLocalError:
                    pass
                except AssertionError:
                    if name is None:
                        logging.error(
                            f'测试步骤二断言结果不正确:添加英雄非正确输入失败用例，hero_name:{name} hero_volume:{volume} hero_power:{power}\n'
                            f'发现问题:新增英雄时如果传参为null可以正常添加')
                    elif isinstance(volume, float) or isinstance(power, float):
                        logging.error(
                            f'测试步骤二断言结果不正确:添加英雄非正确输入失败用例，hero_name:{name} hero_volume:{volume} hero_power:{power}\n'
                            f'发现问题:新增英雄血量和攻击力并非只支持正整数,可以使用浮点数。')
                    raise
