## 蒙地卡羅方法 (Monte Carlo method)
[蒙地卡羅方法](https://wiki.mbalib.com/zh-tw/%E8%92%99%E7%89%B9%E5%8D%A1%E7%BD%97%E6%96%B9%E6%B3%95)
蒙特卡羅方法又稱統計模擬法、隨機抽樣技術，是一種隨機模擬方法，以概率和統計理論方法為基礎的一種計算方法，是使用隨機數（或更常見的偽隨機數）來解決很多計算問題的方法。將所求解的問題同一定的概率模型相聯繫，用電子電腦實現統計模擬或抽樣，以獲得問題的近似解。為象徵性地表明這一方法的概率統計特征，故借用賭城蒙特卡羅命名。
## 黎曼積分
![p](https://github.com/zxc21949049/ai109b/blob/main/pp/ppw1601.png)
## 馬可夫鏈 (Markov chain)
* [馬可夫鏈](https://ithelp.ithome.com.tw/articles/10200869)
Andrey Markov 是一名俄羅斯數學家，主要研究的興趣是隨機程序。馬可夫鏈是馬可夫在研究「一連串相關事件所組成的系統，會怎麼隨著時間變化」時，所提出的一個數學模型。這個模型中有以下部分：

狀態集(states)：包含所有 m 種狀態，記作 https://ithelp.ithome.com.tw/upload/images/20181011/20111741c4a2IhXR1u.png
初始狀態(initial state)：一開始的狀態，記作https://ithelp.ithome.com.tw/upload/images/20181011/20111741dLqtJhxa5V.png
轉移矩陣(transition matrix)：描述上一個狀態，是如何轉移到下一個狀態的，記作 https://ithelp.ithome.com.tw/upload/images/20181011/201117413YE2WkSaGY.png

## 吉布斯採樣 (Gibbs sampling)
* [吉布斯採樣](https://blog.csdn.net/zb1165048017/article/details/51778694)
吉布斯採樣，是統計學中用於馬爾科夫蒙特卡洛（MCMC）的一種算法，用於在難以直接採樣時從某一多變量概率分佈中近似抽取樣本序列。該序列可用於近似聯合分佈、部分變量的邊緣分佈或計算積分（如某一變量的期望值）。某些變量可能為已知變量，故對這些變量並不需要採樣。
![p](https://github.com/zxc21949049/ai109b/blob/main/pp/ppw1602.png)
## 維特比演算法（Viterbi algorithm）
[維特比演算法](https://zh.wikipedia.org/wiki/%E7%BB%B4%E7%89%B9%E6%AF%94%E7%AE%97%E6%B3%95)
維特比演算法是一種動態規劃演算法。它用於尋找最有可能產生觀測事件序列的維特比路徑——隱含狀態序列，特別是在馬可夫資訊源上下文和隱藏式馬可夫模型中。


## EM演算法實作
[EM演算法](https://programmermedia.org/root/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E8%AA%B2%E7%A8%8B/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/06-learn/05-em/em.md)
上述 EM 演算法問題的背後，其實是一種「最大概似估計」，只是加入了「隱變數」的概念，這種「最大概似估計」企圖最大化下列算式中的θ值。

## K-近鄰演算法
[K-近鄰演算法](https://zh.wikipedia.org/wiki/K-%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95)
在圖型識別領域中，最近鄰居法（KNN演算法，又譯K-近鄰演算法）是一種用於分類和迴歸的無母數統計方法。在這兩種情況下，輸入包含特徵空間（Feature Space）中的k個最接近的訓練樣本。