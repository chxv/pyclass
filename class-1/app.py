import mylog


# mylog.info("一个普通消息")

def empty():
    pass  # 一个空函数


def main():
    # mylog.error("一个错误消息")
    mylog.debug(mylog.textualize([1, 2, 3]))
    mylog.debug(mylog.textualize({"a": 1, "b": 2}))
    mylog.debug(mylog.textualize(empty))
    mylog.debug(mylog.textualize(None))


if __name__ == '__main__':
    main()
