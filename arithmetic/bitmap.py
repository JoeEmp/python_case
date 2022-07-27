'''
@Author: your name
@Date: 2020-03-04 10:28:53
@LastEditTime: 2020-03-04 15:48:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /arithmetic/bitmap.py
'''
import logging


def bitmap(bitmap):
    try:
        binstr = bin(bitmap)[:1:-1]
        for i in range(len(binstr)):
            if '1' == binstr[i]:
                yield i
    except Exception as e:
        logging.warning(e)
        return list()


def bitmap_Operation(bitmaps: list, type='and'):
    """bitmap运算

    Arguments:
        bitmaps {list} -- 位图的整数集

    Keyword Arguments:
        type {str} -- and,or,xor (default: {'and'})

    Returns:
        [list] -- 异常是返回list
        [generator] -- 正常返回
    """
    try:
        b = bitmaps[0]
        for i in range(1, len(bitmaps)):
            if 'and' == type:
                b = b & bitmaps[i]
            elif 'or' == type:
                b = b | bitmaps[i]
            elif 'xor' == type:
                b = b ^ bitmaps[i]
    except IndexError:
        return bitmap(b)
    except Exception as e:
        logging.warning(e)
        return bitmaps
    return bitmap(b)


if __name__ == "__main__":
    pass
    l = bitmap_Operation([6,10,2],type='xor',all_range=0)
    print(list(l))
