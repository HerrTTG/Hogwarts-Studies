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


class Test_query():
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.basetest
    @pytest.mark.run(order=2)
    @allure.feature('查询功能')
    @allure.story('查询一般场景')
    @pytest.mark.parametrize("volume", getdate('../datas/query/querynormal_volume.yaml'))
    @pytest.mark.parametrize("name", getdate('../datas/query/querynormal_name.yaml'))
    def test_normal_query(self, objectget, name, volume):
        '''
        发现问题： 查询结果遍历到第一个符合结果就返回true了，
        由于创建时可以重复输入相同name，所以当前查询功能并没有覆盖全部同名数据的查询，retrun的结果只会是第一个。
        '''
        logging.info(f'开始执行用例:查询英雄用例，hero_name:{name} voluem:{volume}')
        allure.dynamic.title(f'查询英雄用例，hero_name:{name} voluem:{volume}')
        with allure.step('测试步骤一,尝试查询英雄'):
            try:
                results = objectget.find_hero(name)
            except:
                logging.error(f'执行查询失败:查询英雄用例，hero_name:{name} voluem:{volume}')
                raise
        with allure.step('测试步骤二,断言结果'):
            try:
                assert results is not False
            except AssertionError:
                logging.error(f'断言失败,查询结果为失败:查询英雄用例，hero_name:{name} voluem:{volume}')
                raise
            else:
                try:
                    assert results['volume'] == volume
                except AssertionError:
                    logging.error(f'断言失败,查询结果与插入的数据不符:查询英雄用例，hero_name:{name} voluem:{volume}\n'
                                  f'发现问题： 查询结果遍历到第一个符合结果就返回true了，由于创建时可以重复输入相同name，所以当前查询功能并没有覆盖全部同名数据的查询，retrun的结果只会是第一个'
                                  f'导致没有返回正确的结果')
                    raise

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.advtest
    @pytest.mark.run(order=2)
    @allure.feature('查询功能')
    @allure.story('查询失败场景')
    @pytest.mark.parametrize("name", getdate('../datas/query/queryraise_name.yaml'))
    def test_raise_query(self, objectget, name):
        logging.info(f'开始执行用例:查询英雄失败用例，hero_name:{name}')
        allure.dynamic.title(f'查询英雄失败用例，hero_name:{name}')
        with allure.step('测试步骤一,尝试查询英雄'):
            try:
                results = objectget.find_hero(name)
            except:
                raise
        with allure.step('测试步骤二,断言结果'):
            assert results is False
