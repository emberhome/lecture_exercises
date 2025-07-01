import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import ReadFromPubSub
from apache_beam import Map
from apache_beam.transforms.window import FixedWindows,TimestampedValue
import os
import time
from datetime import datetime

with beam.Pipeline(options=PipelineOptions(streaming=True)) as pipeline:
    subscription_name = "projects/airy-aria-450311-u1/topics/streaming-lecture-topic"
    data = (
        pipeline
        | "Read Data" >> ReadFromPubSub(topic=subscription_name)
        | "Decode" >> Map(lambda message : message.decode("utf-8"))
        | "Convert to List" >> Map(lambda message : message.split(" "))
    )


    data | "Print" >> Map(print)
