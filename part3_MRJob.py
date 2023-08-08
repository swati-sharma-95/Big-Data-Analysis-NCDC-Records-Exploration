from mrjob.job import MRJob

class MRVisDist(MRJob):

    def mapper(self, _, line):
        val = line.strip()
        (usaf, vis, q) = (val[4:10], val[78:84], val[84:85])
        if (usaf != "999999" and vis != "999999" and q in ['0', '1', '4', '5', '9']):
          yield (int(usaf), int(vis))

    def reducer(self, usaf, vis):
        for vis_dist in vis:
          yield (int(usaf), int(vis_dist))

if __name__ == '__main__':
    MRVisDist.run()
