# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:58:08 2017

@author: whikwon
"""

import pandas as pd
import query_state as qs
import pyodbc

"""Database ���"""

db1 = pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=165.244.114.87;'
    r'DATABASE=LGCOPTMP;'
    r'UID=sa;'
    r'PWD=@admin123'
    )

db2 = pyodbc.connect(
    r'DRIVER={Oracle in OraClient11g_home1};'
    r'DBQ=iepcs;'
    r'UID=iepcs_view;'
    r'PWD=viewdb7388;'   
    )

db3 = pyodbc.connect(
    r'DRIVER={Oracle in OraClient11g_home1};'
    r'DBQ=iegosp;'
    r'UID=iegos_view;'
    r'PWD=viewdb7388;'               
    )

db4 = pyodbc.connect(
    r'DRIVER={Oracle in OraClient11g_home1};'
    r'DBQ=oc_tqms1;'
    r'UID=lqms_view;'
    r'PWD=viewdb7388;'               
    )



def read_lot(start_date, end_date, grade):
    """
    Grade �Ⱓ �� ���� ���� �ҷ�����
    
    Parameters
    ----------
    start_date : ���� ��¥(int or str)
    end_date : ������ ��¥(int or str)
    
    Returns
    -------
    data : ���� ����(dataframe)
        
    """
        
    data = pd.read_sql_query(qs.find_lot(start_date, end_date, grade), db3)
    data.columns = ['����','����','���귮']
    return data
    
    
    
def hq_inspection(start_date, end_date):
    """
    �Ⱓ �� ���� �˻� ���� �ҷ����� 
    
    Parameters
    ----------
    start_date : ���� ��¥(int or str)
    end_Date : ������ ��¥(int or str)
    
    Returns
    -------
    data : ���� ����(dataframe) 
    
    """
    data = pd.read_sql_query(qs.hq_inspection(start_date, end_date), db3)
    return data
    
