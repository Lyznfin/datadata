import csv

from mrjob.job import MRJob
from mrjob.step import MRStep

class MapReduce(MRJob):
    def mapper(self, _, line):
        row = next(csv.reader([line]))
        artist = row[0]
        year = row[1]
        try:
            playcount = int(row[2])
        except:
            playcount = 0
        
        yield (year, artist), playcount

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield None, (sum(values), key)

    def reducer_sorter(self, key, values):
        for count, key in sorted(values):
            yield count, key

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                combiner=self.combiner,
                reducer=self.reducer
            ),
            MRStep(
                reducer=self.reducer_sorter
            )
        ]

def main():
    MapReduce.run()

if __name__ == "__main__":
    main()
    # py get_total_artist_year.py final_sorted_count.csv > artist_count_year.txt