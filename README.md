# input_output_visualize
readtextでファイルを読み込む．
delimiterは区切り記号．csvなら","だけど，コロンとか特定の文字とかでもOK
encodingは指定なしでもよいが文字化けするなら，ファイルのエンコーディングを見て指定すること．utf8とかsjisとか．
ファイルのエンコーディングはメモ帳で保存するときに指定できる．tepaeditorとかnotepad++などの高機能メモ帳を使うとよい．
matplotlibはグラフを書くパッケージ
plt.plot(a)とするとaのデータを折れ線表示する．時刻の情報がある場合，plt.plot(t,a)とするとtにあわせて横軸の目盛りが作成される．
たとえば，t=[1,3,5,10]でa=[1,2,3,4]なら横軸の1,3,5,10のところに1,2,3,4がブロットされる．
plt.subplot(a,b,c)とすると一つのウィンドウに複数のグラフをプロットできる．
