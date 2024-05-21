# -*- coding: utf-8 -*-
"""
preparo las columnas que solo sean tipo int para un manejo mas facil de los calculos
"""
import pandas as pd

# Cargar el conjunto de datos original
data = pd.read_csv('accident.csv')

# Eliminar columnas del DataFrame
columnas_a_eliminar = ['index','accident_id',
                       'ST_CASE','COUNTY',
                       'county_name','CITY',
                       'city_name','HOUR', 'MINUTE',
                       'NHS',
                       'FUNC_SYS',
                       'func_sys_lit',
                       'ROAD_FNC',
                       'road_fnc_lit',
                       'RD_OWNER',
                       'rd_owner_lit',
                       'TWAY_ID',
                       'TWAY_ID2',
                       'LATITUDE',
                       'LONGITUD',
                       'SP_JUR',
                       'sp_jur_lit',
                       'HARM_EV',
                       'harm_ev_lit',
                       'MAN_COLL',
                       'man_coll_lit',
                       'RELJCT1',
                       'RELJCT2',
                       'TYP_INT',
                       'WRK_ZONE',
                       'REL_ROAD',
                       'LGT_COND',
                       'lgt_cond_lit',
                       'WEATHER',
                       'weather_lit',
                       'SCH_BUS',
                       'CF1',
                       'CF2',
                       'CF3',
                       'cf1_lit',
                       'cf2_lit',
                       'cf3_lit',
                       'FATALS',
                       'A_INTER',
                       'a_inter_lit',
                       'A_ROADFC',
                       'a_road_fc_lit',
                       'A_TOD',
                       'a_tod_lit',
                       'A_DOW',
                       'a_dow_lit',
                       'A_LT',
                       'a_lt_lit',
                       'A_SPCRA',
                       'a_spcra_lit',
                       'A_PED',
                       'a_ped_lit',
                       'A_PED_F',
                       'a_ped_f_lit',
                       'A_PEDAL',
                       'a_pedal_lit',
                       'A_PEDAL_F',
                       'a_pedal_f_lit',
                       'A_POLPUR',
                       'a_polour_lit',
                       'A_POSBAC',
                       'a_posbac_lit',
                       'A_DIST',
                       'a_dist_lit',
                       'A_DROWSY',
                       'a_drowsy_lit',
                       'INDIAN_RES',
                       'indian_res_lit']  # Lista con los nombres de las columnas a eliminar
data_numerico = data.drop(columns=columnas_a_eliminar)

# Guardar el DataFrame resultante en un nuevo archivo CSV
data_numerico.to_csv('accidentesnumericos.csv', index=False)

