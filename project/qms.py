# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:16:16 2017

@author: whikwon
"""
import pandas as pd
import query_state as qs
import pyodbc

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


class lqsm():
    """LQMS ���"""
    def read_data(code, start_date, end_date, *items):
        """
        ���� ������ �ҷ��� �� ����Ѵ�.
        
        Parameters
        ----------
        code : ��ǰ �ڵ�(str)
        start_date : ���� ��¥(int|str)
        end_date : ������ ��¥(int|str)
        *items : ���� ��(str) �� �Է� �� ��ü �� ���
        
        Returns
        -------
        X : ������(dataframe)
        
        """
        
        X = pd.read_sql_query(qs.lqms_data(code, start_date, end_date, *items), db4)
        X.columns = ['lot','��ǰ�ڵ�','����','����','n��','������','USL','LSL','����']
        return X