### Colab
![p](https://github.com/zxc21949049/ai109b/blob/main/pp/ppw1501.png)
### RNN 
[循环神经网络 – Recurrent Neural Network | RNN](https://easyai.tech/ai-definition/rnn/)
RNN 的基本原理 傳統神經網絡的結構比較簡單：輸入層 – 隱藏層 – 輸出層。
RNN 跟傳統神經網絡最大的區別在於每次都會將前一次的輸出結果，帶到下一次的隱藏層中，一起訓練
![p](https://github.com/zxc21949049/ai109b/blob/main/pp/ppw1502.png)
RNN 的優化算法 RNN 到 LSTM – 長短期記憶網絡 RNN 是一種死板的邏輯，越晚的輸入影響越大，越早的輸入影響越小，且無法改變這個邏輯。 LSTM 做的最大的改變就是打破了這個死板的邏輯，而改用了一套靈活了邏輯——只保留重要的信息。

LSTM 類似劃重點，他可以保留較長序列數據中的「重要信息」，忽略不重要的信息。
### One-hot Encoding
one hot編碼是將類別變量轉換為機器學習算法易於利用的一種形式的過程。