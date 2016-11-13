def type_study(data):
    """
    测试int类型
    :return:
    >>> type_study(123)
    <class 'int'>

    >>> type_study('abc')
    <class 'str'>

    >>> type_study(None)
    <class 'NoneType'>

    """

    return type(data)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


