import sys
from pyspark import SparkContext

def main():
    sc = SparkContext(appName='SkyCeilingRange')

    input_rdd = sc.textFile('/home/24student24/Course_Project/ProjectData/*')

    filtered_rdd = input_rdd.filter(lambda line: line[70:75] != "99999" and int(line[75:76]) in [0, 1, 4, 5, 9])

    sh_rdd = filtered_rdd.map(lambda line: (line[4:10], int(line[70:75])))

    # Calculate the range of heights for each station ID using reduceByKey
    range_height_rdd = sh_rdd.reduceByKey(lambda x, y: max(x, y) - min(x, y))

    range_height_rdd.saveAsTextFile('/home/24student24/Course_Project/Part2_ProjectOutput/')

    sc.stop()

if __name__ == '__main__':
    main()
