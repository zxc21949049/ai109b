## 人工神經網路
結構（Architecture）結構指定了網路中的變數和它們的拓撲關係。例如，神經網路中的變數可以是神經元連接的權重（weights）和神經元的激勵值（activities of the neurons）。
激勵函式（Activation Rule）大部分神經網路模型具有一個短時間尺度的動力學規則，來定義神經元如何根據其他神經元的活動來改變自己的激勵值。一般激勵函式依賴於網路中的權重（即該網路的參數）。
學習規則（Learning Rule）學習規則指定了網路中的權重如何隨著時間推進而調整。這一般被看做是一種長時間尺度的動力學規則。一般情況下，學習規則依賴於神經元的激勵值。它也可能依賴於監督者提供的目標值和當前權重的值。例如，用於手寫辨識的一個神經網路，有一組輸入神經元。輸入神經元會被輸入圖像的資料所激發。在激勵值被加權並通過一個函式（由網路的設計者確定）後，這些神經元的激勵值被傳遞到其他神經元。這個過程不斷重複，直到輸出神經元被激發。最後，輸出神經元的激勵值決定了辨識出來的是哪個字母。
神經元示意圖
![p](https://github.com/zxc21949049/ai109b/blob/main/pp/ppw901.png)
單層神經元網路
![p](https://github.com/zxc21949049/ai109b/blob/main/pp/ppw902.png)
## 梯度下降法(gradient descent)
梯度下降法(gradient descent)是最佳化理論裡面的一個一階找最佳解的一種方法，主要是希望用梯度下降法找到函數(剛剛舉例的式子)的局部最小值，因為梯度的方向是走向局部最大的方向，所以在梯度下降法中是往梯度的反方向走。
## 練習
* diff.py
```
PS C:\Users\USER\ai\07-neural\02-gradient\01-diff> python diff.py
diff(f,2)= 4.000999999999699
```
* e.py
```
n= 100.0 e(n)= 2.7048138294215285
n= 200.0 e(n)= 2.711517122929317 
n= 300.0 e(n)= 2.7137651579427837
n= 400.0 e(n)= 2.7148917443812293
n= 500.0 e(n)= 2.715568520651728 
n= 600.0 e(n)= 2.7160200488806514
n= 700.0 e(n)= 2.7163427377295566
n= 800.0 e(n)= 2.716584846682471
n= 900.0 e(n)= 2.716773208380411
n= 1000.0 e(n)= 2.7169239322355936
.
.
.
n= 9000.0 e(n)= 2.7181308281830128
n= 9100.0 e(n)= 2.718132487359168
n= 9200.0 e(n)= 2.718134110467929
n= 9300.0 e(n)= 2.718135698675662
n= 9400.0 e(n)= 2.718137253097062
n= 9500.0 e(n)= 2.7181387748001744
n= 9700.0 e(n)= 2.718141724076723
n= 9800.0 e(n)= 2.718143153583405
n= 9900.0 e(n)= 2.718144554210053
n= 10000.0 e(n)= 2.7181459268249255
```
* gd1.py
```
import numpy as np
from numpy.linalg import norm 

# 函數 f 對變數 k 的偏微分: df / dk
def df(f, p, k, step=0.01):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 函數 f 在點 p 上的梯度
def grad(f, p, step=0.01):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, step)
    return gp

# 使用梯度下降法尋找函數最低點
def gradientDescendent(f, p0, step=0.01):
    p = p0.copy()
    i = 0
    while (True):
        i += 1
        fp = f(p)
        gp = grad(f, p) # 計算梯度 gp
        glen = norm(gp) # norm = 梯度的長度 (步伐大小)
        print('{:d}:p={:s} f(p)={:.3f} gp={:s} glen={:.5f}'.format(i, str(p), fp, str(gp), glen))
        if glen < 0.00001:  # 如果步伐已經很小了，那麼就停止吧！
            break
        gstep = np.multiply(gp, -1*step) # gstep = 逆梯度方向的一小步
        p +=  gstep # 向 gstep 方向走一小步
    return p # 傳回最低點！
```
* gdGate.py
```
import numpy as np
import math
import gd3 as gd

def sig(t):
    return 1.0/(1.0+math.exp(-t))

o = [0,0,0,1] # and gate outputs
# o = [0,1,1,1] # or gate outputs
# o = [0,1,1,0] # xor gate outputs
def loss(p, dump=False):
    [w1,w2,b] = p
    o0 = sig(w1*0+w2*0+b)
    o1 = sig(w1*0+w2*1+b)
    o2 = sig(w1*1+w2*0+b)
    o3 = sig(w1*1+w2*1+b)
    delta = np.array([o0-o[0], o1-o[1], o2-o[2], o3-o[3]])
    if dump:
        print('o0={:.3f} o1={:.3f} o2={:.3f} o3={:.3f}'.format(o0,o1,o2,o3))
    return np.linalg.norm(delta, 2)

p = [0.0, 0.0, 0.0] # [w1,w2,b] 
plearn = gd.gradientDescendent(loss, p, max_loops=3000)
loss(plearn, True)

```