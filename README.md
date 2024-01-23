# Project-4-Brevets

This project aims to reimplement the RUSA ACP control time calculator using Flask and AJAX. ACP control times are pivotal for long-distance cyclists participating in Randonneuring events. It determines the minimum and maximum times a rider must reach certain checkpoints (controls) in a given distance.


## Author Information
- **Name:** Deem Alowairdhi
- **QU ID:** 411214706
- **Email:** 411214706@qu.edu.sa

### Objectives:

1. **Understanding the Specs**: One of the primary challenges is to interpret the written specifications from RUSA and translate them into functional code.
  
2. **Unit Testing**: Given the nature of the calculations and their significance in a real-world scenario, it's essential to write unit tests to validate the integrity of the application.

### Dependencies:

- The application is primarily designed for Unix systems, making it more compatible with Linux or macOS. While it might run on Windows, it's not guaranteed. If you're using Windows, consider testing on a Linux virtual machine or a shared server (if available).
  
- A crucial dependency for this project is [docker](https://www.docker.com/products/docker-desktop/). Ensure it's installed on your machine.

### ACP Control Times:

During long-distance cycling events, known as brevets, riders need to prove their passage through specific control points within designated time windows. These time windows, known as controle times, are calculated based on predetermined algorithms. The exact rules for these calculations are available at:

- [ACP Brevet Control Times Calculator](https://rusa.org/pages/acp-brevet-control-times-calculator)
  
- [Rules for Riders](https://rusa.org/pages/rulesForRiders)

The current project aims to replace the existing calculator available [here](https://rusa.org/octime_acp.html). It's recommended to use the above calculator for any cross-reference, clarification of requirements, and to develop test datasets.

### Testing

To ensure the validity and correctness of the ACP control times calculation, a series of tests are included in the project. Here is a glimpse of the testing approach:

```python
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


```

These tests ensure that for given distances and control points, the calculated times match the expected results. It covers various scenarios, from the very start of the brevet to special cases like the French variation for control points less than 60 km.

---
