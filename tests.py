import pytest


class TestBooksCollector:

    def test_init_genre_age_rating_two_genre(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_add_two_books(self, collector, collector_add_book):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_book_zero_len_name(self, collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_book_toolong_len_name(self, collector):
        collector.add_new_book('Рассвет полночи, или Созерцание славы, торжества и мудрости порфироносных, браноносных и мирных гениев России с последованием дидактических, эротических и других разного рода в стихах и прозе опытов Семена Боброва')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_no_genre_for_new_book(self, collector, collector_add_book, book_name):
        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize('new_genre', ['Фантастика', 'Ужасы'])
    def test_test_set_book_genre_in_list_genre(self, collector, collector_add_book, book_name, new_genre):
        collector.set_book_genre(book_name, new_genre)
        assert collector.get_books_with_specific_genre(new_genre) == [book_name]

    def test_set_book_genre_not_in_list_genre(self, collector, collector_add_book, book_name):
        collector.set_book_genre(book_name, 'Что-то странное')
        assert collector.get_book_genre(book_name) == ''

    def test_get_books_for_children_one_of_two(self, collector, collector_add_book, book_name):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre(book_name, 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_for_children() == [book_name]

    def test_add_book_in_favorites_add_book(self, collector, collector_add_book, book_name):
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name]

    def test_delete_book_from_favorites_del_book(self, collector, collector_add_book, book_name):
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert collector.get_list_of_favorites_books() == []
