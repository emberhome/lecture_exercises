import apache_beam as beam

with beam.Pipeline() as pipeline:

  #Read File
  lines = pipeline | 'ReadMyFile' >> beam.io.ReadFromText('log_sample.txt')

  #print lines
  #lines | "Print Lines" >> beam.Map(print)
  #lines | "Print Lines" >> beam.ParDo(lambda x: print(x)) also works

  #find the number of characters in each line
  line_lengths = lines | beam.Map(len)
  #lines is input and line_length is output, goes from right to left

  #print line length
  #line_lengths | "Print Line Lengths" >> beam.Map(print)

  #convert lines to list
  list_lines = lines | "Split" >> beam.Map(lambda x: x.split())

  #print result
  #list_lines | "Print Line Lists" >> beam.Map(print)

  #in order to eventually code the count of each status code, we will first assign a value of 1 to each code, in tuple format
  map_counted = list_lines| "Map" >> beam.Map(lambda x: (x[-1],1))

  #print result
  #map_counted | "Print Tuples" >> beam.Map(print)

  #shuffle elements (so they are grouped by their key, the status code)
  shuffled = map_counted|"Group" >> beam.GroupByKey()

  #print result
  #shuffled | "Print shuffled lines" >> beam.Map(print)

  #Reduce
  reduced = shuffled | "Reduce" >> beam.Map(lambda x: (x[0],sum(x[1])))

  #write result to file
  reduced | "Write to Text File" >> beam.io.WriteToText('output.txt')
