import time
import pandas as pd
import MetaTrader5 as mt5
import datetime


# OPCÕES DE DEZEMBRO


def petrdezembro():
    for a in opcoes_petrodez[0], opcoes_petrodez[2], opcoes_petrodez[4], opcoes_petrodez[6], opcoes_petrodez[8], \
             opcoes_petrodez[10]:
        x = mt5.copy_rates_from(a, mt5.TIMEFRAME_D1, data, dias)
        x = pd.DataFrame(x)
        # x = x.drop(x.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;33m', a, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x)
        custo = PETR - x
        print('\033[1;31mcusto\033[m')
        print(custo)
        print('\033[1;36mproteção\033[m')
        protecao = PETR / custo
        protecao['Total'] = protecao['close'] - 1.02
        print(protecao)
        print('\033[1;33mprêmio\033[m')
        if a == opcoes_petrodez[0]:
            premio = Zpetrdez / custo
            premio['total'] = premio['close'] - 1.02
            print(premio)
        elif a == opcoes_petrodez[2]:
            premio1 = Zpetr1dez / custo
            premio1['total'] = premio1['close'] - 1.02
            print(premio1)
        elif a == opcoes_petrodez[4]:
            premio2 = Zpetr2dez / custo
            premio2['total'] = premio2['close'] - 1.02
            print(premio2)
        elif a == opcoes_petrodez[6]:
            premio3 = Zpetr3dez / custo
            premio3['total'] = premio3['close'] - 1.02
            print(premio3)
        elif a == opcoes_petrodez[8]:
            premio4 = Zpetr4dez / custo
            premio4['total'] = premio4['close'] - 1.02
            print(premio4)
        elif a == opcoes_petrodez[10]:
            premio5 = Zpetr5dez / custo
            premio5['total'] = premio5['close'] - 1.02
            print(premio5)
        print('\033[1;30m-#\033[m' * 4)
        time.sleep(2)
        print('\033[1;30m-#\033[m' * 4)


def ambevdezembro():
    for b in opcoes_ambevdez[0], opcoes_ambevdez[2], opcoes_ambevdez[4], opcoes_ambevdez[6], opcoes_ambevdez[8], \
             opcoes_ambevdez[10]:
        x1 = mt5.copy_rates_from(b, mt5.TIMEFRAME_D1, data, dias)
        x1 = pd.DataFrame(x1)
        x1 = x1.drop(x1.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;32m', b, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x1)
        custo2 = ABEV - x1
        print('\033[1;31mcusto\033[m')
        print(custo2)
        print('\033[1;36mproteção\033[m')
        protecao2 = ABEV / custo2
        protecao2['total'] = protecao2['close'] - 1.02
        print(protecao2)
        print('\033[1;33mprêmio\033[m')
        if b == opcoes_ambevdez[0]:
            premioabev = Zabevdez / custo2
            premioabev['total'] = premioabev['close'] - 1.02
            print(premioabev)
        elif b == opcoes_ambevdez[2]:
            premioabev1 = Zabev1dez / custo2
            premioabev1['total'] = premioabev1['close'] - 1.02
            print(premioabev1)
        elif b == opcoes_ambevdez[4]:
            premioabev2 = Zabev2dez / custo2
            premioabev2['total'] = premioabev2['close'] - 1.02
            print(premioabev2)
        elif b == opcoes_ambevdez[6]:
            premioabev3 = Zabev3dez / custo2
            premioabev3['total'] = premioabev3['close'] - 1.02
            print(premioabev3)
        elif b == opcoes_ambevdez[8]:
            premioabev4 = Zabev4dez / custo2
            premioabev4['total'] = premioabev4['close'] - 1.02
            print(premioabev4)
        elif b == opcoes_ambevdez[10]:
            premioabev5 = Zabev5dez / custo2
            premioabev5['total'] = premioabev5['close'] - 1.02
            print(premioabev5)
        time.sleep(4)
        print('\033[1;30m-#\033[m' * 4)


def bovdezembro():
    for c in opcoes_b3SAdez[0], opcoes_b3SAdez[2], opcoes_b3SAdez[4], opcoes_b3SAdez[6], opcoes_b3SAdez[8], \
             opcoes_b3SAdez[10]:
        x2 = mt5.copy_rates_from(c, mt5.TIMEFRAME_D1, data, dias)
        x2 = pd.DataFrame(x2)
        x2 = x2.drop(x2.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;34m', c, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x2)
        custo3 = B3SA - x2
        print('\033[1;31mcusto\033[m')
        print(custo3)
        print('\033[1;36mproteção\033[m')
        protecao3 = B3SA / custo3
        protecao3['Total'] = protecao3['close'] - 1.02
        print(protecao3)
        print('\033[1;33mprêmio\033[m')
        if c == opcoes_b3SAdez[0]:
            premioB3SA = ZB3SAdez / custo3
            premioB3SA['total'] = premioB3SA['close'] - 1.02
            print(premioB3SA)
        elif c == opcoes_b3SAdez[2]:
            premioB3SA1 = ZB3SA1dez / custo3
            premioB3SA1['total'] = premioB3SA1['close'] - 1.02
            print(premioB3SA1)
        elif c == opcoes_b3SAdez[4]:
            premioB3SA2 = ZB3SA2dez / custo3
            premioB3SA2['total'] = premioB3SA2['close'] - 1.02
            print(premioB3SA2)
        elif c == opcoes_b3SAdez[6]:
            premioB3SA3 = ZB3SA3dez / custo3
            premioB3SA3['total'] = premioB3SA3['close'] - 1.02
            print(premioB3SA3)
        elif c == opcoes_b3SAdez[8]:
            premioB3SA4 = ZB3SA4dez / custo3
            premioB3SA4['total'] = premioB3SA4['close'] - 1.02
            print(premioB3SA4)
        elif c == opcoes_b3SAdez[10]:
            premioB3SA5 = ZB3SA5dez / custo3
            premioB3SA5['total'] = premioB3SA5['close'] - 1.02
            print(premioB3SA5)
        print('\033[1;30m-#\033[m' * 4)
        time.sleep(4)


def usimdezembro():
    for d in opcoes_usiminasdez[0], opcoes_usiminasdez[2], opcoes_usiminasdez[4], opcoes_usiminasdez[6], \
             opcoes_usiminasdez[8], opcoes_usiminasdez[10]:
        x3 = mt5.copy_rates_from(d, mt5.TIMEFRAME_D1, data, dias)
        x3 = pd.DataFrame(x3)
        x3 = x3.drop(x3.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;35m', d, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x3)
        custo4 = USIM - x3
        print('\033[1;31mcusto\033[m')
        print(custo4)
        print('\033[1;36mproteção\033[m')
        protecao4 = USIM / custo4
        protecao4['Total'] = protecao4['close'] - 1.02
        print(protecao4)
        print('\033[1;33mprêmio\033[m')
        if d == opcoes_usiminasdez[0]:
            premioUSIM = ZUSIMdez / custo4
            premioUSIM['total'] = premioUSIM['close'] - 1.02
            print(premioUSIM)
        elif d == opcoes_usiminasdez[2]:
            premioUSIM1 = ZUSIM1dez / custo4
            premioUSIM1['total'] = premioUSIM1['close'] - 1.02
            print(premioUSIM1)
        elif d == opcoes_usiminasdez[4]:
            premioUSIM2 = ZUSIM2dez / custo4
            premioUSIM2['total'] = premioUSIM2['close'] - 1.02
            print(premioUSIM2)
        elif d == opcoes_usiminasdez[6]:
            premioUSIM3 = ZUSIM3dez / custo4
            premioUSIM3['total'] = premioUSIM3['close'] - 1.02
            print(premioUSIM3)
        elif d == opcoes_usiminasdez[8]:
            premioUSIM4 = ZUSIM4dez / custo4
            premioUSIM4['total'] = premioUSIM4['close'] - 1.02
            print(premioUSIM4)
        elif d == opcoes_usiminasdez[10]:
            premioUSIM5 = ZUSIM5dez / custo4
            premioUSIM5['total'] = premioUSIM5['close'] - 1.02
            print(premioUSIM5)
        print('\033[1;30m-#\033[m' * 4)
        time.sleep(4)


def ggbrdezembro():
    for e in opcoes_gerdaudez[0], opcoes_gerdaudez[2], opcoes_gerdaudez[4], opcoes_gerdaudez[6], opcoes_gerdaudez[8], \
             opcoes_gerdaudez[10]:
        x4 = mt5.copy_rates_from(e, mt5.TIMEFRAME_D1, data, dias)
        x4 = pd.DataFrame(x4)
        x4 = x4.drop(x4.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;36m', e, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x4)
        custo5 = GGBR4 - x4
        print('\033[1;31mcusto\033[m')
        print(custo5)
        print('\033[1;36mproteção\033[m')
        protecao5 = GGBR4 / custo5
        protecao5['Total'] = protecao5['close'] - 1.02
        print(protecao5)
        print('\033[1;33mprêmio\033[m')
        if e == opcoes_gerdaudez[0]:
            premioGGBR = ZGGBRdez / custo5
            premioGGBR['total'] = premioGGBR['close'] - 1.02
            print(premioGGBR)
        elif e == opcoes_gerdaudez[2]:
            premioGGBR1 = ZGGBR1dez / custo5
            premioGGBR1['total'] = premioGGBR1['close'] - 1.02
            print(premioGGBR1)
        elif e == opcoes_gerdaudez[4]:
            premioGGBR2 = ZGGBR2dez / custo5
            premioGGBR2['total'] = premioGGBR2['close'] - 1.02
            print(premioGGBR2)
        elif e == opcoes_gerdaudez[6]:
            premioGGBR3 = ZGGBR3dez / custo5
            premioGGBR3['total'] = premioGGBR3['close'] - 1.02
            print(premioGGBR3)
        elif e == opcoes_gerdaudez[8]:
            premioGGBR4 = ZGGBR4dez / custo5
            premioGGBR4['total'] = premioGGBR4['close'] - 1.02
            print(premioGGBR4)
        elif e == opcoes_gerdaudez[10]:
            premioGGBR5 = ZGGBR5dez / custo5
            premioGGBR5['total'] = premioGGBR5['close'] - 1.02
            print(premioGGBR5)
        print('\033[1;30m-#\033[m' * 4)
        time.sleep(4)


def valedezembro():
    for f in opcoes_valedez[0], opcoes_valedez[2], opcoes_valedez[4], opcoes_valedez[6], opcoes_valedez[8], \
             opcoes_valedez[10]:
        x5 = mt5.copy_rates_from(f, mt5.TIMEFRAME_D1, data, dias)
        x5 = pd.DataFrame(x5)
        x5 = x5.drop(x5.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;31m', f, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x5)
        custo6 = VALE3 - x5
        print('\033[1;31mcusto\033[m')
        print(custo6)
        print('\033[1;36mproteção\033[m')
        protecao6 = VALE3 / custo6
        protecao6['Total'] = protecao6['close'] - 1.02
        print(protecao6)
        print('\033[1;33mprêmio\033[m')
        if f == opcoes_valedez[0]:
            premioVALE = ZVALEdez / custo6
            premioVALE['total'] = premioVALE['close'] - 1.02
            print(premioVALE)
        elif f == opcoes_valedez[2]:
            premioVALE1 = ZVALE1dez / custo6
            premioVALE1['total'] = premioVALE1['close'] - 1.02
            print(premioVALE1)
        elif f == opcoes_valedez[4]:
            premioVALE2 = ZVALE2dez / custo6
            premioVALE2['total'] = premioVALE2['close'] - 1.02
            print(premioVALE2)
        elif f == opcoes_valedez[6]:
            premioVALE3 = ZVALE3dez / custo6
            premioVALE3['total'] = premioVALE3['close'] - 1.02
            print(premioVALE3)
        elif f == opcoes_valedez[8]:
            premioVALE4 = ZVALE4dez / custo6
            premioVALE4['total'] = premioVALE4['close'] - 1.02
            print(premioVALE4)
        elif f == opcoes_valedez[10]:
            premioVALE5 = ZVALE5dez / custo6
            premioVALE5['total'] = premioVALE5['close'] - 1.02
            print(premioVALE5)
        print('\033[1;30m-#\033[m' * 4)
        time.sleep(4)


# OPÇÕES DE JANEIRO


def petrjaneiro():
    for a in opcoes_petrojan[0], opcoes_petrojan[2], opcoes_petrojan[4], opcoes_petrojan[6], opcoes_petrojan[8], \
             opcoes_petrojan[10]:
        x = mt5.copy_rates_from(a, mt5.TIMEFRAME_D1, data, dias)
        x = pd.DataFrame(x)
        x = x.drop(x.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;33m', a, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x)
        custo = PETR - x
        print('\033[1;31mcusto\033[m')
        print(custo)
        print('\033[1;36mproteção\033[m')
        protecao = PETR / custo
        protecao['Total'] = protecao['close'] - 1.02
        print(protecao)
        print('\033[1;33mprêmio\033[m')
        if a == opcoes_petrojan[0]:
            premio = Zpetrjan / custo
            premio['total'] = premio['close'] - 1.02
            print(premio)
        elif a == opcoes_petrojan[2]:
            premio1 = Zpetr1jan / custo
            premio1['total'] = premio1['close'] - 1.02
            print(premio1)
        elif a == opcoes_petrojan[4]:
            premio2 = Zpetr2jan / custo
            premio2['total'] = premio2['close'] - 1.02
            print(premio2)
        elif a == opcoes_petrojan[6]:
            premio3 = Zpetr3jan / custo
            premio3['total'] = premio3['close'] - 1.02
            print(premio3)
        elif a == opcoes_petrojan[8]:
            premio4 = Zpetr4jan / custo
            premio4['total'] = premio4['close'] - 1.02
            print(premio4)
        elif a == opcoes_petrojan[10]:
            premio5 = Zpetr5jan / custo
            premio5['total'] = premio5['close'] - 1.02
            print(premio5)
        print('\033[1;30m-#\033[m' * 4)
        time.sleep(2)
        print('\033[1;30m-#\033[m' * 4)


def ambevjaneiro():
    for b in opcoes_ambevjan[0], opcoes_ambevjan[2], opcoes_ambevjan[4], opcoes_ambevjan[6], opcoes_ambevjan[8], \
             opcoes_ambevjan[10]:
        x1 = mt5.copy_rates_from(b, mt5.TIMEFRAME_D1, data, dias)
        x1 = pd.DataFrame(x1)
        x1 = x1.drop(x1.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;32m', b, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x1)
        custo2 = ABEV - x1
        print('\033[1;31mcusto\033[m')
        print(custo2)
        print('\033[1;36mproteção\033[m')
        protecao2 = ABEV / custo2
        protecao2['total'] = protecao2['close'] - 1.02
        print(protecao2)
        print('\033[1;33mprêmio\033[m')
        if b == opcoes_ambevjan[0]:
            premioabev = Zabevjan / custo2
            premioabev['total'] = premioabev['close'] - 1.02
            print(premioabev)
        elif b == opcoes_ambevjan[2]:
            premioabev1 = Zabev1jan / custo2
            premioabev1['total'] = premioabev1['close'] - 1.02
            print(premioabev1)
        elif b == opcoes_ambevjan[4]:
            premioabev2 = Zabev2jan / custo2
            premioabev2['total'] = premioabev2['close'] - 1.02
            print(premioabev2)
        elif b == opcoes_ambevjan[6]:
            premioabev3 = Zabev3jan / custo2
            premioabev3['total'] = premioabev3['close'] - 1.02
            print(premioabev3)
        elif b == opcoes_ambevjan[8]:
            premioabev4 = Zabev4jan / custo2
            premioabev4['total'] = premioabev4['close'] - 1.02
            print(premioabev4)
        elif b == opcoes_ambevjan[10]:
            premioabev5 = Zabev5jan / custo2
            premioabev5['total'] = premioabev5['close'] - 1.02
            print(premioabev5)
        time.sleep(4)
        print('\033[1;30m-#\033[m' * 4)


def bovjaneiro():
    for c in opcoes_b3SAjan[0], opcoes_b3SAjan[2], opcoes_b3SAjan[4], opcoes_b3SAjan[6], opcoes_b3SAjan[8], \
             opcoes_b3SAjan[10]:
        x2 = mt5.copy_rates_from(c, mt5.TIMEFRAME_D1, data, dias)
        x2 = pd.DataFrame(x2)
        x2 = x2.drop(x2.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;34m', c, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x2)
        custo3 = B3SA - x2
        print('\033[1;31mcusto\033[m')
        print(custo3)
        print('\033[1;36mproteção\033[m')
        protecao3 = B3SA / custo3
        protecao3['Total'] = protecao3['close'] - 1.02
        print(protecao3)
        print('\033[1;33mprêmio\033[m')
        if c == opcoes_b3SAjan[0]:
            premioB3SA = ZB3SAjan / custo3
            premioB3SA['total'] = premioB3SA['close'] - 1.02
            print(premioB3SA)
        elif c == opcoes_b3SAjan[2]:
            premioB3SA1 = ZB3SA1jan / custo3
            premioB3SA1['total'] = premioB3SA1['close'] - 1.02
            print(premioB3SA1)
        elif c == opcoes_b3SAjan[4]:
            premioB3SA2 = ZB3SA2jan / custo3
            premioB3SA2['total'] = premioB3SA2['close'] - 1.02
            print(premioB3SA2)
        elif c == opcoes_b3SAjan[6]:
            premioB3SA3 = ZB3SA3jan / custo3
            premioB3SA3['total'] = premioB3SA3['close'] - 1.02
            print(premioB3SA3)
        elif c == opcoes_b3SAjan[8]:
            premioB3SA4 = ZB3SA4jan / custo3
            premioB3SA4['total'] = premioB3SA4['close'] - 1.02
            print(premioB3SA4)
        elif c == opcoes_b3SAjan[10]:
            premioB3SA5 = ZB3SA5jan / custo3
            premioB3SA5['total'] = premioB3SA5['close'] - 1.02
            print(premioB3SA5)
        print('\033[1;30m-#\033[m' * 4)
        time.sleep(4)


def usimjaneiro():
    for d in opcoes_usiminasjan[0], opcoes_usiminasjan[2], opcoes_usiminasjan[4], opcoes_usiminasjan[6], \
             opcoes_usiminasjan[8], opcoes_usiminasjan[10]:
        x3 = mt5.copy_rates_from(d, mt5.TIMEFRAME_D1, data, dias)
        x3 = pd.DataFrame(x3)
        x3 = x3.drop(x3.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;35m', d, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x3)
        custo4 = USIM - x3
        print('\033[1;31mcusto\033[m')
        print(custo4)
        print('\033[1;36mproteção\033[m')
        protecao4 = USIM / custo4
        protecao4['Total'] = protecao4['close'] - 1.02
        print(protecao4)
        print('\033[1;33mprêmio\033[m')
        if d == opcoes_usiminasjan[0]:
            premioUSIM = ZUSIMjan / custo4
            premioUSIM['total'] = premioUSIM['close'] - 1.02
            print(premioUSIM)
        elif d == opcoes_usiminasjan[2]:
            premioUSIM1 = ZUSIM1jan / custo4
            premioUSIM1['total'] = premioUSIM1['close'] - 1.02
            print(premioUSIM1)
        elif d == opcoes_usiminasjan[4]:
            premioUSIM2 = ZUSIM2jan / custo4
            premioUSIM2['total'] = premioUSIM2['close'] - 1.02
            print(premioUSIM2)
        elif d == opcoes_usiminasjan[6]:
            premioUSIM3 = ZUSIM3jan / custo4
            premioUSIM3['total'] = premioUSIM3['close'] - 1.02
            print(premioUSIM3)
        elif d == opcoes_usiminasjan[8]:
            premioUSIM4 = ZUSIM4jan / custo4
            premioUSIM4['total'] = premioUSIM4['close'] - 1.02
            print(premioUSIM4)
        elif d == opcoes_usiminasjan[10]:
            premioUSIM5 = ZUSIM5jan / custo4
            premioUSIM5['total'] = premioUSIM5['close'] - 1.02
            print(premioUSIM5)
        print('\033[1;30m-#\033[m' * 4)
        time.sleep(4)


def ggbrjaneiro():
    for e in opcoes_gerdaujan[0], opcoes_gerdaujan[2], opcoes_gerdaujan[4], opcoes_gerdaujan[6], opcoes_gerdaujan[8], \
             opcoes_gerdaujan[10]:
        x4 = mt5.copy_rates_from(e, mt5.TIMEFRAME_D1, data, dias)
        x4 = pd.DataFrame(x4)
        x4 = x4.drop(x4.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;36m', e, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x4)
        custo5 = GGBR4 - x4
        print('\033[1;31mcusto\033[m')
        print(custo5)
        print('\033[1;36mproteção\033[m')
        protecao5 = GGBR4 / custo5
        protecao5['Total'] = protecao5['close'] - 1.02
        print(protecao5)
        print('\033[1;33mprêmio\033[m')
        if e == opcoes_gerdaujan[0]:
            premioGGBR = ZGGBRjan / custo5
            premioGGBR['total'] = premioGGBR['close'] - 1.02
            print(premioGGBR)
        elif e == opcoes_gerdaujan[2]:
            premioGGBR1 = ZGGBR1jan / custo5
            premioGGBR1['total'] = premioGGBR1['close'] - 1.02
            print(premioGGBR1)
        elif e == opcoes_gerdaujan[4]:
            premioGGBR2 = ZGGBR2jan / custo5
            premioGGBR2['total'] = premioGGBR2['close'] - 1.02
            print(premioGGBR2)
        elif e == opcoes_gerdaujan[6]:
            premioGGBR3 = ZGGBR3jan / custo5
            premioGGBR3['total'] = premioGGBR3['close'] - 1.02
            print(premioGGBR3)
        elif e == opcoes_gerdaujan[8]:
            premioGGBR4 = ZGGBR4jan / custo5
            premioGGBR4['total'] = premioGGBR4['close'] - 1.02
            print(premioGGBR4)
        elif e == opcoes_gerdaujan[10]:
            premioGGBR5 = ZGGBR5jan / custo5
            premioGGBR5['total'] = premioGGBR5['close'] - 1.02
            print(premioGGBR5)
        print('\033[1;30m-#\033[m' * 4)
        time.sleep(4)


def valejaneiro():
    for f in opcoes_valejan[0], opcoes_valejan[2], opcoes_valejan[4], opcoes_valejan[6], opcoes_valejan[8], \
             opcoes_valejan[10]:
        x5 = mt5.copy_rates_from(f, mt5.TIMEFRAME_D1, data, dias)
        x5 = pd.DataFrame(x5)
        x5 = x5.drop(x5.columns[[0, 1, 2, 3, 5, 6, 7]], axis=1)
        print('\033[1;31m', f, ':\033[m')
        print('\033[1;33mcotação\033[m')
        print(x5)
        custo6 = VALE3 - x5
        print('\033[1;31mcusto\033[m')
        print(custo6)
        print('\033[1;36mproteção\033[m')
        protecao6 = VALE3 / custo6
        protecao6['Total'] = protecao6['close'] - 1.02
        print(protecao6)
        print('\033[1;33mprêmio\033[m')
        if f == opcoes_valejan[0]:
            premioVALE = ZVALEjan / custo6
            premioVALE['total'] = premioVALE['close'] - 1.02
            print(premioVALE)
        elif f == opcoes_valejan[2]:
            premioVALE1 = ZVALE1jan / custo6
            premioVALE1['total'] = premioVALE1['close'] - 1.02
            print(premioVALE1)
        elif f == opcoes_valejan[4]:
            premioVALE2 = ZVALE2jan / custo6
            premioVALE2['total'] = premioVALE2['close'] - 1.02
            print(premioVALE2)
        elif f == opcoes_valejan[6]:
            premioVALE3 = ZVALE3jan / custo6
            premioVALE3['total'] = premioVALE3['close'] - 1.02
            print(premioVALE3)
        elif f == opcoes_valejan[8]:
            premioVALE4 = ZVALEjan / custo6
            premioVALE4['total'] = premioVALE4['close'] - 1.02
            print(premioVALE4)
        elif f == opcoes_valejan[10]:
            premioVALE5 = ZVALE5jan / custo6
            premioVALE5['total'] = premioVALE5['close'] - 1.02
            print(premioVALE5)
        print('\033[1;30m-#\033[m' * 4)
        time.sleep(4)


if not mt5.initialize():
    print('tivemos um problema na inicialização do mts', mt5.last_error())
    quit()
dias = 1
data = time.time()
carteira_closes = pd.DataFrame()
hoje = datetime.date.today()

# STRIKES DE DEZEMBRO

opcoes_petrodez = ['PETRL396', 26.77,
                   'PETRL331', 27.02,
                   'PETRL311', 26.27,
                   'PETRL38', 27.77,
                   'PETRL308', 25.52,
                   'PETRL411', 28.02]
opcoes_ambevdez = ['ABEVL161', 15.64,
                   'ABEVL158', 15.89,
                   'ABEVL159', 16.14,
                   'ABEVL163', 16.34,
                   'ABEVL166', 16.64,
                   'ABEVL173', 17.34]
opcoes_b3SAdez = ['B3SAL122', 12.26,
                  'B3SAL125', 12.51,
                  'B3SAL130', 13.01,
                  'B3SAL442', 13.26,
                  'B3SAL135', 13.51,
                  'B3SAL140', 14.01]
opcoes_usiminasdez = ['USIML766', 7.66,
                      'USIML786', 7.86,
                      'USIML796', 7.96,
                      'USIML806', 8.06,
                      'USIML836', 8.36,
                      'USIML906', 9.06]
opcoes_gerdaudez = ['GGBRL301', 30.11,
                    'GGBRL311', 31.11,
                    'GGBRL318', 30.61,
                    'GGBRL320', 31.36,
                    'GGBRL328', 31.61,
                    'GGBRL321', 32.11]
opcoes_valedez = ['VALEL794', 79.41,
                  'VALEL803', 80.41,
                  'VALEL842', 80.91,
                  'VALEL824', 82.41,
                  'VALEL862', 82.91,
                  'VALEL867', 83.41]

# STRIKES DE JANEIRO

opcoes_petrojan = ['PETRA321', 25.51,
                   'PETRA351', 26.27,
                   'PETRA368', 27.27,
                   'PETRA378', 28.77,
                   'PETRA356', 29.02,
                   'PETRA357', 29.52]
opcoes_ambevjan = ['ABEVA165', 16.57,
                   'ABEVA160', 16.07,
                   'ABEVA148', 14.82,
                   'ABEVA153', 15.32,
                   'ABEVA155', 15.57,
                   'ABEVA173', 17.32]
opcoes_b3SAjan = ['B3SAA117', 11.64,
                  'B3SAA122', 12.14,
                  'B3SAA137', 13.64,
                  'B3SAA135', 13.14,
                  'B3SAA126', 12.64,
                  'B3SAA151', 15.14]
opcoes_usiminasjan = ['USIMA720', 7.20,
                      'USIMA760', 7.60,
                      'USIMA780', 7.80,
                      'USIMA800', 8.00,
                      'USIMA820', 8.20,
                      'USIMA900', 9.00]
opcoes_gerdaujan = ['GGBRA273', 27.36,
                    'GGBRA296', 29.61,
                    'GGBRA308', 30.11,
                    'GGBRA306', 30.61,
                    'GGBRA32', 31.11,
                    'GGBRA316', 31.61]
opcoes_valejan = ['VALEA822', 78.91,
                  'VALEA103', 82.41,
                  'VALEA844', 77.41,
                  'VALEA101', 80.41,
                  'VALEA105', 84.41,
                  'VALEA887', 85.41]

# X = cotação ação, Y = cotação da opção, Z = strike, N = quantidade de ações
# custo = X - Y * n
# proteção = (((X / custo) -1) *100)
# prêmio = (((Z / custo) -1) * 100)

# VARIÁVEL DOS STRIKES DE DEZEMBRO

Zpetrdez = opcoes_petrodez[1]
Zpetr1dez = opcoes_petrodez[3]
Zpetr2dez = opcoes_petrodez[5]
Zpetr3dez = opcoes_petrodez[7]
Zpetr4dez = opcoes_petrodez[9]
Zpetr5dez = opcoes_petrodez[11]
#########################
Zabevdez = opcoes_ambevdez[1]
Zabev1dez = opcoes_ambevdez[3]
Zabev2dez = opcoes_ambevdez[5]
Zabev3dez = opcoes_ambevdez[7]
Zabev4dez = opcoes_ambevdez[9]
Zabev5dez = opcoes_ambevdez[11]
#########################
ZB3SAdez = opcoes_b3SAdez[1]
ZB3SA1dez = opcoes_b3SAdez[3]
ZB3SA2dez = opcoes_b3SAdez[5]
ZB3SA3dez = opcoes_b3SAdez[7]
ZB3SA4dez = opcoes_b3SAdez[9]
ZB3SA5dez = opcoes_b3SAdez[11]
########################
ZUSIMdez = opcoes_usiminasdez[1]
ZUSIM1dez = opcoes_usiminasdez[3]
ZUSIM2dez = opcoes_usiminasdez[5]
ZUSIM3dez = opcoes_usiminasdez[7]
ZUSIM4dez = opcoes_usiminasdez[9]
ZUSIM5dez = opcoes_usiminasdez[11]
############################
ZGGBRdez = opcoes_gerdaudez[1]
ZGGBR1dez = opcoes_gerdaudez[3]
ZGGBR2dez = opcoes_gerdaudez[5]
ZGGBR3dez = opcoes_gerdaudez[7]
ZGGBR4dez = opcoes_gerdaudez[9]
ZGGBR5dez = opcoes_gerdaudez[11]
##########################
ZVALEdez = opcoes_valedez[1]
ZVALE1dez = opcoes_valedez[3]
ZVALE2dez = opcoes_valedez[5]
ZVALE3dez = opcoes_valedez[7]
ZVALE4dez = opcoes_valedez[9]
ZVALE5dez = opcoes_valedez[11]
########################

# VARIÁVEL DOS STRIKES DE JANEIRO

Zpetrjan = opcoes_petrojan[1]
Zpetr1jan = opcoes_petrojan[3]
Zpetr2jan = opcoes_petrojan[5]
Zpetr3jan = opcoes_petrojan[7]
Zpetr4jan = opcoes_petrojan[9]
Zpetr5jan = opcoes_petrojan[11]
#########################
Zabevjan = opcoes_ambevjan[1]
Zabev1jan = opcoes_ambevjan[3]
Zabev2jan = opcoes_ambevjan[5]
Zabev3jan = opcoes_ambevjan[7]
Zabev4jan = opcoes_ambevjan[9]
Zabev5jan = opcoes_ambevjan[11]
#########################
ZB3SAjan = opcoes_b3SAjan[1]
ZB3SA1jan = opcoes_b3SAjan[3]
ZB3SA2jan = opcoes_b3SAjan[5]
ZB3SA3jan = opcoes_b3SAjan[7]
ZB3SA4jan = opcoes_b3SAjan[9]
ZB3SA5jan = opcoes_b3SAjan[11]
########################
ZUSIMjan = opcoes_usiminasjan[1]
ZUSIM1jan = opcoes_usiminasjan[3]
ZUSIM2jan = opcoes_usiminasjan[5]
ZUSIM3jan = opcoes_usiminasjan[7]
ZUSIM4jan = opcoes_usiminasjan[9]
ZUSIM5jan = opcoes_usiminasjan[11]
############################
ZGGBRjan = opcoes_gerdaujan[1]
ZGGBR1jan = opcoes_gerdaujan[3]
ZGGBR2jan = opcoes_gerdaujan[5]
ZGGBR3jan = opcoes_gerdaujan[7]
ZGGBR4jan = opcoes_gerdaujan[9]
ZGGBR5jan = opcoes_gerdaujan[11]
##########################
ZVALEjan = opcoes_valejan[1]
ZVALE1jan = opcoes_valejan[3]
ZVALE2jan = opcoes_valejan[5]
ZVALE3jan = opcoes_valejan[7]
ZVALE4jan = opcoes_valejan[9]
ZVALE5jan = opcoes_valejan[11]


########################
# n = int(input('Quantidade de ações: '))


def opcoeseacoes(acao, opcao):
    print('\033[1;37m-#\033[m' * 15)
    print('\033[1;37m', acao, ':\033[m')
    acao = mt5.copy_rates_from(acao, mt5.TIMEFRAME_D1, data, dias)
    acao = pd.DataFrame(acao)
    #acao = acao.drop(acao.columns[[0, 1, 2, 3, 5, 6]], axis=1)
    print(acao)
    print('\033[1;37m', opcao, ':\033[m')
    opcao = mt5.copy_rates_from(opcao, mt5.TIMEFRAME_D1, data, dias)
    opcao = pd.DataFrame(opcao)
    #opcao = opcao.drop(opcao.columns[[0, 1, 2, 3, 5, 6]], axis=1)
    print('\033[1;32m')
    opcao['Prêmio'] = (opcao['close'] / acao['close']) * 100
    print(opcao)
    print('\033[1;37m-#\033[m' * 15)
    print('')
    print('')
    print('')
    time.sleep(5)


while True:
    # COTAÇÕES
    # cotação da PETR4
    #     opcoeseacoes('PETR4')
    PETR = mt5.copy_rates_from('PETR4', mt5.TIMEFRAME_D1, data, dias)
    # cotação da ABEV3
    #     opcoeseacoes('ABEV3')
    ABEV = mt5.copy_rates_from('ABEV3', mt5.TIMEFRAME_D1, data, dias)
    # cotação da USIM5
    # opcoeseacoes('USIM5')
    USIM = mt5.copy_rates_from('USIM3', mt5.TIMEFRAME_D1, data, dias)
    # cotação da BOVESPA
    # opcoeseacoes('B3SA3')
    B3SA = mt5.copy_rates_from('B3SA3', mt5.TIMEFRAME_D1, data, dias)
    # cotação da GGBR4
    # opcoeseacoes('GGBR4')
    GGBR4 = mt5.copy_rates_from('GGBR4', mt5.TIMEFRAME_D1, data, dias)
    # cotação da VALE3
    # opcoeseacoes('VALE3')
    VALE3 = mt5.copy_rates_from('VALE3', mt5.TIMEFRAME_D1, data, dias)
    # OPÇÕES
    # print('=' * 15)
    # print('\033[1mopções de dezembro: \033[m')
    # opções da PETR4 de dezembro
    # petrdezembro()

    # opções da AMBEV de dezembro
    # ambevdezembro()

    # opções da B3SA de dezembro
    # bovdezembro()

    # opções da USIM de dezembro
    # usimdezembro()

    # opções da GGBR de dezembro
    # ggbrdezembro()

    # opções da VALE de dezembro
    # valedezembro()

    ############################
    # print('\033[1mopções de janeiro: \033[m')
    # opções da PETR4 de janeiro
    # petrjaneiro()

    # opções da AMBEV de janeiro
    # ambevjaneiro()

    # opções da B3SA de janeiro
    # bovjaneiro()

    # opções da USIM de janeiro
    # usimjaneiro()

    # opções da GGBR de janeiro
    # ggbrjaneiro()

    # opções da VALE de janeiro
    # valejaneiro()

#OPÇÕES CALL
    # opcoeseacoes('ITSAN884')
    # opcoeseacoes('ITSAN864')
    # opcoeseacoes('BBSEN369')
    # opcoeseacoes('BBSEN379')

    # opcoeseacoes('CPLEN760') INDISPONIVEL
    # opcoeseacoes('CPLEN810') INDISPONIVEL
    # opcoeseacoes('KLBNN200') INDISPONIVEL
    # opcoeseacoes('KLBNN190') INDISPONIVEL
    break

#opções put
while True:
    opcoeseacoes('ITSA4', 'ITSAO887')
    opcoeseacoes('ITSA4', 'ITSAO872')
    opcoeseacoes('ITSA4', 'ITSAO978')
    opcoeseacoes('GGBR4', 'GGBRO289')
    opcoeseacoes('GGBR4', 'GGBRO282')
    opcoeseacoes('GGBR4', 'GGBRO284')
    opcoeseacoes('BBAS3', 'BBASO440')
    opcoeseacoes('BBAS3', 'BBASO427')
    opcoeseacoes('BBAS3', 'BBASO425')

# opcoeseacoes('SANB11', 'SANBO300') INDISPONÍVEL
# opcoeseacoes('SANB11', 'SANBO295') INDISPONÍVEL
# opcoeseacoes('SANB11', 'SANBO305') INDISPONÍVEL
# opcoeseacoes('TAEE11', 'TAEE0377') INDISPONÍVEL
# opcoeseacoes('TAEE11', 'TAEEO372') INDISPONÍVEL
# opcoeseacoes('TAEE11', 'TAEEO382') INDISPONÍVEL


