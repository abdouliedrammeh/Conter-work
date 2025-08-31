from counter import counter
from db import get_db, add_counter, increment_counter, get_counter_date
from analysis import calculate_count

class TestCounter:

    def setuo_method(self):
        self.db = get_db("test.db")

        add_counter(self.db, "test_counter", "test_description")
        increment_counter(self.db, "test_counter", "2024-12-06")
        increment_counter(self.db, "test_counter", "2024-12-07")


        increment_counter(self.db, "test_counter", "2023-12-08")
        increment_counter(self.db, "test_counter", "2023-12-09")

    def test_counter(self):
        counter= counter ("test_counter_1", "test_description_1")
        counter.store (self.db)
        
        counter.increment()
        counter.add_event(self.db)
        counter.reset()
        counter.increment()

    def test_db_counter(self):
        date = get_counter_date(self.db, "test_counter")
        assert len(date) == 4

        count= calculate_count(self.db, "test_count")


    def teardown_method(self):
        import os
        os.remove("test.db")