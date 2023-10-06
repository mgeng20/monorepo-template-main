# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 5, 10)]
        gilded_rose = GildedRose(items)

        original_sell_in = gilded_rose.get_item_sell_in("foo")
        original_quality = gilded_rose.get_item_quality("foo")
        gilded_rose.update_quality()
        new_sell_in = gilded_rose.get_item_sell_in("foo")
        new_quality = gilded_rose.get_item_quality("foo")
        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 1

    def test_aged_brie(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        original_sell_in = gilded_rose.get_item_sell_in("Aged Brie")
        original_quality = gilded_rose.get_item_quality("Aged Brie")

        gilded_rose.update_quality()
        new_sell_in = gilded_rose.get_item_sell_in("Aged Brie")
        new_quality = gilded_rose.get_item_quality("Aged Brie")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality > original_quality
        assert new_quality == original_quality + 1

    def test_backstage_passes_1(self):
        items = [Item("Backstage passes", 10, 20)]
        gilded_rose = GildedRose(items)

        original_sell_in = gilded_rose.get_item_sell_in("Backstage passes")
        original_quality = gilded_rose.get_item_quality("Backstage passes")

        gilded_rose.update_quality()

        new_sell_in = gilded_rose.get_item_sell_in("Backstage passes")
        new_quality = gilded_rose.get_item_quality("Backstage passes")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality > original_quality
        assert new_quality == original_quality + 2

    def test_backstage_passes_2(self):
        items = [Item("Backstage passes", 5, 20)]
        gilded_rose = GildedRose(items)

        original_sell_in = gilded_rose.get_item_sell_in("Backstage passes")
        original_quality = gilded_rose.get_item_quality("Backstage passes")

        gilded_rose.update_quality()

        new_sell_in = gilded_rose.get_item_sell_in("Backstage passes")
        new_quality = gilded_rose.get_item_quality("Backstage passes")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality > original_quality
        assert new_quality == original_quality + 3

    def test_backstage_passes_3(self):
        items = [Item("Backstage passes", 0, 20)]
        gilded_rose = GildedRose(items)

        original_sell_in = gilded_rose.get_item_sell_in("Backstage passes")
        original_quality = gilded_rose.get_item_quality("Backstage passes")

        gilded_rose.update_quality()

        new_sell_in = gilded_rose.get_item_sell_in("Backstage passes")
        new_quality = gilded_rose.get_item_quality("Backstage passes")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1
        assert original_quality > 0
        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality == 0

    def test_backstage_passes_4(self):
        items = [Item("Backstage passes", 15, 20)]
        gilded_rose = GildedRose(items)

        original_sell_in = gilded_rose.get_item_sell_in("Backstage passes")
        original_quality = gilded_rose.get_item_quality("Backstage passes")

        gilded_rose.update_quality()

        new_sell_in = gilded_rose.get_item_sell_in("Backstage passes")
        new_quality = gilded_rose.get_item_quality("Backstage passes")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality > original_quality
        assert new_quality == original_quality + 1

    def test_sulfuras(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        original_sell_in = gilded_rose.get_item_sell_in("Sulfuras")
        original_quality = gilded_rose.get_item_quality("Sulfuras")
        gilded_rose.update_quality()
        new_sell_in = gilded_rose.get_item_sell_in("Sulfuras")
        new_quality = gilded_rose.get_item_quality("Sulfuras")

        assert new_sell_in == original_sell_in
        assert new_quality == original_quality
        assert original_quality == 80

    def test_conjured_item(self):
        # Arrange
        items = [Item("Conjured", 5, 42)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Conjured")
        original_quality = gr.get_item_quality("Conjured")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Conjured")
        new_quality = gr.get_item_quality("Conjured")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 2


if __name__ == '__main__':
    unittest.main()
