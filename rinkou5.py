import os
import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt



def read_file(first_file, second_file, third_file):
    df1 = pd.read_csv(first_file, sep='\t', skiprows=6, index_col='Strand shift')
    df2 = pd.read_csv(second_file, sep='\t', skiprows=6, index_col='Strand shift')
    df3 = pd.read_csv(third_file, sep='\t', skiprows=6, index_col='Strand shift')

    return df1, df2, df3
    # ファイルを３つ読み込んでいる

# extract legend name except ".jaccrd.csv"
def legend_name(first_file, second_file, third_file):
    filename_list = [first_file, second_file, third_file]
    legend_list = []
    for f in filename_list:
        name = os.path.basename(f)
        legend_list.append(name.split(".", 1)[0])

    return legend_list
    # 保存用に、ファイル名を取り出している。for文を使って回している。
    # basenameで基部を取得、さらにsplitで1を指定してドットの上を得るというアクロバティック技
    # 得られた名前は一旦filename_listとしてリスト形式で保存している。


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="make figure of per control from test 3 data")
    parser.add_argument("first", help="first file path", type=str)
    parser.add_argument("second", help="second file path", type=str)
    parser.add_argument("third", help="third file path", type=str)
    parser.add_argument("-n","--newfile", help="new file name", type=str, default="rinkou5.pdf")
# argparseで３つのファイルを読み込む。--newfileで、保存ファイル名を指定できるようにしている。
# オプションなので、--newfileで指定しなければdefaultの"rinkou5.pdf"として保存される。


    args = parser.parse_args()

    first_file = args.first
    second_file = args.second
    third_file = args.third
    newfile = args.newfile

    df1, df2, df3 = read_file(first_file, second_file, third_file)
    # こんなふうにまとめられるんや！
    legend_list = legend_name(first_file, second_file, third_file)

    plt.figure(figsize=(4,4))
    plt.plot(df1.iloc[:,3], label=legend_list[0], color="red")
    plt.plot(df2.iloc[:,3], label=legend_list[1], color="blue")
    plt.plot(df3.iloc[:,3], label=legend_list[2], color="black")
    plt.xlim(0,500)
    plt.xlabel("index")
    plt.ylabel("per control")
    plt.legend(loc='upper right')
    plt.savefig(newfile)
