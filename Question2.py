
def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    import math

    small = 0                                            #配列の先頭
    big = len(sorted_array) - 1                          #配列の最後尾
    time = int(math.ceil(math.log2(len(sorted_array))))  #計算回数をlog2nの小数点以下切り上げにより決定

    for n in range(1, time + 1):                         #time回探索を行う
        center = (small + big) // 2

        #print(center)

        if sorted_array[center] == target_number:
            return target_number                         #sorted_array[center]がtarget_numberと一致したので終了

        elif sorted_array[center] < target_number:
            small = center + 1                           #centerより先頭側に範囲を絞る

        else:
            big = center - 1                             #centerより後尾側に範囲を絞る

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
