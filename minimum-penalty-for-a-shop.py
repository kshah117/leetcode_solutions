class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_suffix = customers.count("Y")
        n_prefix = 0
        min_pen = y_suffix
        index = -1
        for i, c in enumerate(customers):
            if c == "Y":
                y_suffix -= 1
            else:
                n_prefix += 1

            pen = y_suffix + n_prefix

            if pen < min_pen:
                index = i
                min_pen = pen

        return index + 1
