#这是一段Python代码
#MC群峦TFC锻造计算器
#作者：lcxs
#QQ:2979283511

#定义部分

def HeFa1(X):
    '''
    判断倒数第X目标是否合法.若合法输出True.
    '''
    if X!=int(11) and X!=int(12) and X!=int(13) and X!=int(14) and X!=int(21) and X!=int(22) and X!=int(23) and X!=int(24) and X!=int(0):
        return False
    else:
        return True

def HeFa2(X):
    '''
    判断输入的数字是否在0到150之间.若是.输出True
    '''
    if X>=int(0) and X<=(150):
        return True
    else:
        return False

def ZhuanHuanZhengShu(X):
    '''
    将倒数目标代数转换为真实整数.即转换为对应的数字.例如11是‘击打’即转换为-3.
    '''
    if X ==int(11):
        X=-3
        return X
    elif X ==int(12):
        X=-6
        return X
    elif X ==int(13):
        X=2
        return X
    elif X ==int(14):
        X=7
        return X
    elif X ==int(21):
        X=-9
        return X
    elif X ==int(22):
        X=-15
        return X
    elif X ==int(23):
        X=13
        return X
    elif X ==int(0):
        X=0
        return X
    
    else:
        X=16
        return X

def ZhuanHuanHanZi(X):
    '''
    将倒数目标代数转换为对应的名称
    '''
    if X == int(11):
        X = '轻击 '
    elif X == int(12):
        X = '击打 '
    elif X == int(13):
        X = '冲压 '
    elif X == int(14):
        X = '弯曲 '
    elif X == int(21):
        X = '重击 '
    elif X == int(22):
        X = '牵拉 '
    elif X == int(23):
        X = '镦锻 '
    elif X == int(24):
        X = '收缩 '
    elif X == int(0):
        X =''
    else:
        X = 'err '
    return X 

#输入部分

print('-----------------------------------------------')
print('程序启动！')

while True:

    while True:
        print('-----------------------------------------------')
        print('0任意方法')
        print('11轻击 12击打 13冲压 14弯曲 ')
        print('21重击 22牵拉 23镦锻 24收缩 ')
        print('-----------------------------------------------')
        D1 = int(input('请输入倒数第一个方法:'))
        if HeFa1(D1)==True:
            break
        print('输入错误!')

    while True:
        D2 = int(input('请输入倒数第二个方法:'))
        if HeFa1(D2)==True:
            break
        print('输入错误!')

    while True:
        D3 = int(input('请输入倒数第三个方法:'))
        if HeFa1(D3)==True:
            break
        print('输入错误!')
    
    while True:
        S1 = int(input('请输入目标点数:'))
        if HeFa2(S1)==True:
            break
        print('输入错误!')

    while True:
        S2 = int(input('请输入起始点数：'))
        if HeFa2(S2)==True:
            break
        print('输入错误！')

#计算部分

    #反推去掉倒数三步后的点数，即进行完倒数第四步后所剩的点数.
    R1 = S1 - ZhuanHuanZhengShu(D1) - ZhuanHuanZhengShu(D2) -ZhuanHuanZhengShu(D3) - S2
    
    #大于零的情况
    #if R1>= int(0):
    if True: 
        #取进行完倒数第四步后所剩的点数整除收缩数，即所需‘收缩’步数.
        Q1 = R1 // int(16)
        #计算进行‘收缩’步数后剩下的点数.
        Q2 = R1 - (Q1*int(16))
        #将剩下点数的所有可能根据以下步骤进行配凑，即进行完以下步骤后点数正好可以等于进行完倒数第四步后所剩的点数.
        if Q2==int(0):#以下是我配凑出的方法，可能不是最简，如果你有更好的算法方法请告诉我.
            W = '○'
        elif Q2==int(1):#例如：弯曲（+7）击打（-6）后，（+7）+（-6）=+1，整体步数+1.
            W = '①弯曲 击打 '
        elif Q2==int(2):
            W = '②冲压 '
        elif Q2==int(3):
            W = '③冲压 弯曲 击打 '
        elif Q2==int(4):
            W = '④冲压 冲压 '
        elif Q2==int(5):
            W = '⑤镦锻 弯曲 牵拉 '
        elif Q2==int(6):
            W = '⑥冲压 冲压 冲压 '
        elif Q2==int(7):
            W = '⑦弯曲 '
        elif Q2==int(8):
            W = '⑧弯曲 收缩 牵拉 '
        elif Q2==int(9):
            W = '⑨冲压 弯曲 '
        elif Q2==int(10):
            W = '⑩镦锻 轻击 '
        elif Q2==int(11):
            W = '⑪镦锻 弯曲 重击 '
        elif Q2==int(12):
            W = '⑫镦锻 冲压 轻击 '
        elif Q2==int(13):
            W = '⑬镦锻 '
        elif Q2==int(14):
            W = '⑭弯曲 弯曲 '
        elif Q2==int(15):
            W = '⑮收缩 冲压 牵拉 '
        else:
            print('error')
    
    #小于零的情况
    #if R1<= int(0):
        #将结果取绝对值
        #R1 = -R1
        #计算

    #将倒数三步的数字代数转换为汉字.
    A1 = ZhuanHuanHanZi(D1)
    A2 = ZhuanHuanHanZi(D2)
    A3 = ZhuanHuanHanZi(D3)
    print('-----------------------------------------------')
    print('计算完毕：' + '收缩 ' * Q1 + W + A3 + A2 + A1)