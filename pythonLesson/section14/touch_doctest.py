class Cal(object):
    def add_num_and_double(self, x, y):
        """Addn and double
        
        >>> c = Cal()
        >>> c.add_num_and_double(1,1)
        4

        >>> c.add_num_and_double('1', '1')
        Traceback (most recent call last):
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result


# ドキュメント+やり方を見せるくらいのテスト
# 本格的な運用では使わないけど、簡単な処理例を載せるのに使う

if __name__ == "__main__":
    import doctest

    doctest.testmod()
