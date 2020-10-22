import os
import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="make figure of testdir")
    parser.add_argument("dirname", help="first file path", type=str)
    # inputのディレクトリ名、必須
    parser.add_argument("-n","--newdir", help="new output dir", type=str, default="output")
    # outputのディレクトリ名、--newdirで指定、入れないければdefaultのoutputとなる

    args = parser.parse_args()

    dpath = args.dirname
    files_name = os.listdir(dpath)
    # os.listdir()で、ファイル名の一覧を取得

    new_dir = args.newdir
    os.makedirs(new_dir, exist_ok=True)
    # os.mkdirsは、深い階層のディレクトリまで再帰的に作成するコマンド。
    # 引数でexist_ok = Trueとすると、既に存在しているディレクトリを指定してもエラーにならない。

    for file in files_name:
        # 取得したファイル名の一覧についてfor文を回す
        file_path = dpath + file
        # ディレクトリ名とファイル名を結合してfile_pathとする
        df = pd.read_csv(file_path, sep='\t', skiprows=6, index_col='Strand shift')
        # 変数dfに読み込み

        plt.figure(figsize=(4,4))
        plt.plot(df.iloc[:,3], color="red")
        plt.xlim(0,500)
        plt.xlabel("index")
        plt.ylabel("per control")

        newfigure = file.split(".", 1)[0]
        # ファイル名はやはりアクロバティック技で取得

        plt.savefig(new_dir + "/" + newfigure + ".pdf")
        # plt.savefig()で、ファイルをpath指定して保存
        plt.close()
        # plt.close()で、figureのウインドウを閉じる
        # たぶん、closeしなくても20個くらいならいける。
        # closeしないと、メモリの関係で、これ以上開けてられません！というエラーになる。
