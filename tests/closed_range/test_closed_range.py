#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

class TestClosedRange:
    @pytest.fixture()
    def closed_range(self):
        from closed_range.closed_range import ClosedRange
        return ClosedRange(3,8)

    def test_下端点3を持つ(self,closed_range):
        assert closed_range.lower_limit == 3

    def test_上限点8を持つ(self,closed_range):
        assert closed_range.upper_limit == 8

    def test_下端点3かつ上端点8の整数閉区間の配列表現を文字列化して返す(self,closed_range):
        assert str(closed_range) == "[3,8]"

    def test_下端点8かつ上端点3の閉区間を作ることはできない(self):
        from closed_range.closed_range import ClosedRange
        with pytest.raises(ValueError) as e:
            _ = ClosedRange(8,3)

    def test_下端点3上端点8が整数5を含むかどうかを判定できる(self,closed_range):
        assert closed_range.is_included(5)

    class Test別の閉区間と等価かどうか判定できる():
        def test_閉区間3から8と閉区間3から8が等価かどうか判定できる(self):
            from closed_range.closed_range import ClosedRange
            closed_range_1 = ClosedRange(3,8)
            closed_range_2 = ClosedRange(3,8)
            assert closed_range_1 == closed_range_2

        def dynamic_params():
            from closed_range.closed_range import ClosedRange
            return [
            (ClosedRange(2,5),'下限点2も上限点5も等価でない'),
            (ClosedRange(3,4),'下限点3は等価だが、上限点4は等価でない'),
            (ClosedRange(1,8),'上限点1は等価だが、下限点8は等価でない'),
            ]

        @pytest.mark.parametrize("closed_range_2, desc", dynamic_params())
        def test_閉区間3から8と別の閉区間が等価でないことを判定できる(self, closed_range,closed_range_2,desc):
            closed_range_1 = closed_range
            assert closed_range_1 != closed_range_2

    class Test別の閉区間を完全に含むか判定できる():
        def test_閉区間3から8が閉区間4から7を含むか判定できる(self):
            from closed_range.closed_range import ClosedRange
            closed_range_1 = ClosedRange(3,8)
            closed_range_2 = ClosedRange(4,7)

            assert closed_range_1.is_included(closed_range_2)

        def test_閉区間3から8が閉区間2から9を含むか判定できる(self):
            from closed_range.closed_range import ClosedRange
            closed_range_1 = ClosedRange(3,8)
            closed_range_2 = ClosedRange(2,9)

            assert not closed_range_1.is_included(closed_range_2)