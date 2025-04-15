"""
impotrs
"""

import pandasai as pdai
from pandasai import SmartDataframe
from openai import OpenAI
from cfg import AI_Config
from pandasai_litellm import LiteLLM
from pywebio.input import file_upload,input
from pywebio.output import put_text, put_markdown,put_loading,toast

from io import BytesIO
import pandas as pd
import os
from dotenv import load_dotenv


def app():
    load_dotenv()
    put_markdown("## 数据分析助手 ##")
    put_text("目前正处于开发测试阶段，支持excel文件分析")
    xlfile = file_upload(
        "请上传文件（目前支持xlsx或xls文件）",
        accept=".xlsx, .xls",
        required=True
    )
    df = pd.read_excel(BytesIO(xlfile["content"]))

    put_markdown("## 数据预览 ##")
    put_text(df.head())

    put_markdown("## 数据分析 ##")
    config = AI_Config(model = "deepseek-reasoner",
                       base_url = "https://api.deepseek.com/v1",
                       api_key = os.getenv("DS_API_KEY")
    )
    if not config.api_key:
        raise ValueError("api-key 配置错误")
    prompt = input("请输入你的指令:如请帮我找出其中最大的数字")


    output = analyseExcel(df, prompt, config)

    put_text(output)

def analyseExcel(df:pd.DataFrame,prompt:str,config:AI_Config):
    df_pdai = pdai.DataFrame(df)
    llm = LiteLLM(model=config.model,
                           api_base=config.base_url,
                           api_key=config.api_key
    )
    pdai.config.set({"llm":llm})
    with put_loading(shape='grow', color='primary'):
        toast("正在分析中，请稍后...",duration=0)
        output = df_pdai.chat(prompt)
    return output


