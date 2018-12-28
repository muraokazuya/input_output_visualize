import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt("filename", delimiter=",", encoding="sjis") #encoding must be your file encoding
plt.subplots_adjust(wspace=0.4, hspace=0.6)#文字サイズを変えるとグラフどうしが重なるので，これを指定するとうまいこと調整してくれる．
plt.subplot(2,3,1) #subplotの設定．引数は順番に横の列数，縦の行数，左上から開始した右方向への通し番号
plt.title("graph 1") #グラフのタイトル
plt.plot(a) # データの表示（以下同様）
plt.subplot(2,3,2)
plt.title("graph 2")
plt.plot(a)
plt.subplot(2,3,3)
plt.title("graph 3")
plt.plot(a)
plt.subplot(2,3,4)
plt.title("graph 4")
plt.plot(a)
plt.subplot(2,3,5)
plt.title("graph 5")
plt.plot(a)
plt.subplot(2,3,6)
plt.title("graph 6")
plt.plot(a)
plt.rcParams["font.size"] = 24 #文字サイズの変更
plt.show()
