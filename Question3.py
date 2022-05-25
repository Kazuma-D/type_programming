def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    save = 0                #値交換用
    start = 0               #配列の先頭
    end = len(array) - 1    #配列の末端


    while 1:
        while start <= len(array) - 1 and array[start] < pivot:
            start = start + 1                                   #基準値より大きい値を先頭から検索

        while end >= 0 and array[end] >= pivot:
            end = end - 1                                       #基準値より小さい値を末端から検索

        if start >= end:
            break                                               #検索がぶつかったら処理終了

        save = array[start]                                     #この３行で
        array[start] = array[end]                               #値を
        array[end] = save                                       #入れ替える


    left = []
    right = []                                                  #グループ分けのための配列を用意

    for j in range(0,start):
        left.append(array[j])                                   #先頭から検索がぶつかった場所までの値をグループ化
    for k in range(start ,len(array)):
        right.append(array[k])                                  #検索がぶつかった場所から末端までの値をグループ化

    #print(left , right)

    if end >= 0:
        left = sort(left)
        right = sort(right)                                     #交換する部分がなくなるまで再帰的に繰り返し


    return left + right                                         #ソート結果を返す

    # ここまで記述

if __name__ == '__main__':
    main()
