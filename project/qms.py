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


class lqms():
    """LQMS ���"""
    def read_data(prod_wc_cd, prod_cd, start_date, end_date, *items):
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
        
        X = pd.read_sql_query(qs.lqms_data(prod_wc_cd, prod_cd, start_date, end_date, *items), db4)        
        X.columns = ['lot','��ǰ�ڵ�','����','����','n��','������','USL','LSL','����']
        X[['������','USL','LSL']] = X[['������','USL','LSL']].astype(float)
        return X
        
        
def Cpk(data,d2=1.693):
    """
    Cpk ���� �� ����Ѵ�.
    
    Parameters
    ----------
    data : ���� ������(dataframe)
    d2 : 1.693 (n = 3) / 1.128 (n = 2)
    
    Returns
    -------
    Cpk : Cpk��(float)
    
    """
    
    usl = data['USL'].dropna().drop_duplicates()
    lsl = data['LSL'].dropna().drop_duplicates()
    if len(usl) + len(lsl) != 2:            
        raise Exception('USL, LSL�� 2�� �̻� �ְų� �����ϴ�. ���� grade, code���� Ȯ���غ�����.')
        
    else:
        usl, lsl = usl[0], lsl[0]

    sigma = (data.groupby('lot')['������'].max() - data.groupby('lot')['������'].min()).mean()/d2
    m = data['������'].mean()
    Cpu = float(usl - m) / (3*sigma)
    Cpl = float(m - lsl) / (3*sigma)
    Cpk = min([Cpu, Cpl])
    return Cpk
    
    
def Ppk(data):
    """
    Ppk ���� �� ����Ѵ�.
    
    Paramters
    ---------
    data : ���� ������(dataframe)
    
    Returns
    -------
    Ppk : Ppk��(float)
    
    """
    
    usl = data['USL'].dropna().drop_duplicates()
    lsl = data['LSL'].dropna().drop_duplicates()
    if len(usl) + len(lsl) != 2:            
        raise Exception('USL, LSL�� 2�� �̻� �ְų� �����ϴ�. ���� grade, code���� Ȯ���غ�����.')
        
    else:
        usl, lsl = usl[0], lsl[0]
    sigma = data['������'].std()
    m = data['������'].mean()
    Ppu = float(usl - m) / (3*sigma)
    Ppl = float(m - lsl) / (3*sigma)
    Ppk = min([Ppu, Ppl])
    return Ppk
    
        
        



        