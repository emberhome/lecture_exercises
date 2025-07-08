import aiofiles
import asyncio
import time

async def read_file(file_name):
    print(f"Reading file {file_name}...")
    start_time = time.perf_counter()
    async with aiofiles.open(file_name, mode='r') as f:
        bytes = await f.read()
        print(f"Read file with length {len(bytes)} in {time.perf_counter() - start_time:0.2f} seconds.")

async def process_data(file_names):
    total_start_time = time.perf_counter()
    tasks = [read_file(file_name) for file_name in file_names]
    await asyncio.gather(*tasks)
    print(f"Processed all files in {time.perf_counter() - total_start_time:0.2f} seconds.")

if __name__ == '__main__':
    list_of_files = ['news.csv','news.csv','news.csv']
    asyncio.run(process_data(list_of_files))
