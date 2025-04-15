"""
一个基于网页开发的数据分析助手：
先基于excel进行开发
"""


from cfg import AI_Config
import pandasai as pdai
from pandasai_litellm import LiteLLM
from data_analyse import analyseExcel, app
from pywebio import start_server
"""
imports
"""

if __name__ == "__main__":
    start_server(app, port=8080)
