def main (data,context):processes= ("download_pytrends.py","upload_gcs.py","remove_files.py")for p in processes:
exec(open(p).read())if __name__ == "__main__":main('data','context')
