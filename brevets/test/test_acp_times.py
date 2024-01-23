import acp_times
import arrow
import nose

class TestControlTimes:

    def setUp(self):
        self.start_date = arrow.Arrow(2023, 10, 10)

    def test_open_and_close_for_mid_range_distance(self):
        """Testing open and close times for a control point at 150 km on a 200 km brevet."""
        assert acp_times.open_time(150, 200, self.start_date) == (self.start_date.shift(hours=4, minutes=25)).isoformat()
        assert acp_times.close_time(150, 200, self.start_date) == (self.start_date.shift(hours=10)).isoformat()

    def test_large_distance_within_1000_km_brevet(self):
        """Testing open and close times for a control point at 700 km on a 1000 km brevet."""
        assert acp_times.open_time(700, 1000, self.start_date) == (self.start_date.shift(hours=22, minutes=22)).isoformat()
        assert acp_times.close_time(700, 1000, self.start_date) == (self.start_date.shift(hours=48, minutes=45)).isoformat()

    def test_exact_control_at_end_of_600_km_brevet(self):
        """Testing open and close times for the last control point of a 600 km brevet."""
        assert acp_times.open_time(600, 600, self.start_date) == (self.start_date.shift(hours=18, minutes=48)).isoformat()
        assert acp_times.close_time(600, 600, self.start_date) == (self.start_date.shift(hours=40)).isoformat()

    def test_regular_mid_range_control_within_600_km_brevet(self):
        """Testing open and close times for a control point at 550 km on a 600 km brevet."""
        assert acp_times.open_time(550, 600, self.start_date) == (self.start_date.shift(hours=17, minutes=8)).isoformat()
        assert acp_times.close_time(550, 600, self.start_date) == (self.start_date.shift(hours=36, minutes=40)).isoformat()

    def test_odd_distance_within_400_km_brevet(self):
        """Testing open and close times for a control point at 311 km on a 400 km brevet."""
        assert acp_times.open_time(311, 400, self.start_date) == (self.start_date.shift(hours=9, minutes=21)).isoformat()
        assert acp_times.close_time(311, 400, self.start_date) == (self.start_date.shift(hours=20, minutes=44)).isoformat()

    def test_start_of_brevet(self):
        """Testing open and close times at the very start of a 200 km brevet."""
        assert acp_times.open_time(0, 200, self.start_date) == self.start_date.isoformat()
        assert acp_times.close_time(0, 200, self.start_date) == (self.start_date.shift(hours=1)).isoformat()

    def test_french_variation_for_control_less_than_60_km(self):
        """Testing open and close times for a control point at 55 km, considering the French variation."""
        assert acp_times.open_time(55, 600, self.start_date) == (self.start_date.shift(hours=1, minutes=37)).isoformat()
        assert acp_times.close_time(55, 600, self.start_date) == (self.start_date.shift(hours=3, minutes=45)).isoformat()

    def test_close_time_for_control_less_than_60_km(self):
        """Testing only the close time for a control point at 40 km."""
        assert acp_times.close_time(40, 600, self.start_date) == (self.start_date.shift(hours=3)).isoformat()


if __name__ == '__main__':
    nose.run(argv=['', __file__])
