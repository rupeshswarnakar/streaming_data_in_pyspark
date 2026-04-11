# Read Streaming Data
df = spark.readStream.format("delta").table("emp")

# Process Each Batch
import uuid

def foreach_batch_function(df, epoch_id):
    df.write.json("/tmp/output2/" + str(uuid.uuid4()))
    df.collect()

df.writeStream.foreachBatch(foreach_batch_function).start()

# Checkpointing Example
import uuid

def foreach_batch_function(df, epoch_id):
    array_id = df.collect()[0][0]

    if array_id == 12:
        raise Exception("Stopping the streaming")

    df.write.json("/tmp/output9/" + str(uuid.uuid4()))
    df.collect()

df.writeStream \
    .option("checkpointLocation", "/tmp/checkpoint/2") \
    .foreachBatch(foreach_batch_function) \
    .start()

# Start Stream from Specific Version
spark.readStream.format("delta") \
    .option("startingVersion", "5")

# Start Stream from Specific Timestamp
spark.readStream.format("delta") \
    .option("startingTimestamp", "2018-10-18")

