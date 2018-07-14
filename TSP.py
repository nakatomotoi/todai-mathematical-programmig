import numpy as np
import pandas as pd
from pandas import DataFrame
import math
import copy


route_list = [
    [math.inf,21,7,13,15],
    [11,math.inf,19,12,25],
    [15,24,math.inf,13,5],
    [6,17,9,math.inf,22],
    [28,6,11,5,math.inf]
]

route_df = DataFrame(route_list)
ans_value = []
ans_route = []

def getMinRoute(df):
    minimum = 1000
    loc = [-1,-1]
    for index in df.index:
        for column in df.columns:
            if(df.loc[index,column]==math.inf):
                continue
            if(df.loc[index,column]<minimum):
                minimum = df.loc[index,column]
                loc = [index,column]
    return loc

def getGekai1(df,loc):
    minimum = df.loc[loc[0],loc[1]]
    # 採用するルートを元の行列から除く
    if(loc[1] in df.index and loc[0] in df.columns):
        df.loc[loc[1],loc[0]] = math.inf
    df.drop(index=loc[0],axis=0,inplace=True)
    df.drop(columns=loc[1],axis=1,inplace=True)
    # 各行の最小値を求め、その値を引いた値を各行に返す
    min_list_row = df.min(axis=1).values
    df_tmp = df.sub(min_list_row,axis=0)
    min_list_column = df_tmp.min().values
    df_tmp = df_tmp.sub(min_list_column,axis=1)
    gekai = min_list_row.sum()+min_list_column.sum()+sum(ans_value)+minimum
    return gekai

def getGekai2(df,loc):
    df.loc[loc[0],loc[1]] = math.inf
    min_list_row = df.min(axis=1).values
    df = df.sub(min_list_row,axis=0)
    min_list_column = df.min().values
    df = df.sub(min_list_column,axis=1)
    gekai = min_list_row.sum()+min_list_column.sum()+sum(ans_value)
    return gekai

while(True):
    if(len(route_df.index)==1):
        loc = [route_df.index[0],route_df.columns[0]]
        ans_route.append(loc)
        ans_value.append(df.loc[loc[0],loc[1]])
        break
    df = route_df.copy()
    df2 = route_df.copy()
    loc = getMinRoute(route_df)
    minimum = df.loc[loc[0],loc[1]]
    if(getGekai1(df,loc)<=getGekai2(df2,loc)):
        getGekai1(route_df,loc)
        ans_value.append(minimum)
        ans_route.append(loc)
    else:
        getGekai2(route_df,loc)

def print_route(r):
    print(r[0][0]+1,"->")
    print(r[0][1]+1,"->")
    node = r[0][1]
    for i in range(len(r)-1):
        for route in r:
            if(route[0]==node):
                print(route[1]+1,"->")
                node = route[1]
                break


print("route_distance",sum(ans_value))
print_route(ans_route)
